# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This repository currently contains a single Python module, `comet_4.py`, with no package manifest, test suite, linter config, or build tooling. There is no `requirements.txt`/`pyproject.toml` — the only external dependency is `httpx`, which must be installed manually (`pip install httpx`) before the module can be imported or run.

There are no build, lint, or test commands to document yet, since none exist in the repo. If you add tooling (tests, linting, packaging), update this section accordingly.

## What `comet_4.py` does

A standalone async client for the Comet API (`https://api.cometapi.com/v1`), an OpenAI-compatible image generation API. It's built for "series" work — generating many related images (e.g. per-cut/scene images for a storyboard) in one batch, with results durably logged as they complete.

### Configuration (env vars)

All behavior is tuned via environment variables, read once at import time as module-level constants:

- `COMET_BASE_URL` (default `https://api.cometapi.com/v1`)
- `COMET_API_KEY` — required; `generate_comet` raises `RuntimeError` if unset
- `COMET_IMAGE_MODEL` (default `flux-pro`) — varies by account (e.g. `sdxl`)
- `COMET_TIMEOUT` (default `180` sec)
- `COMET_RESPONSE_FORMAT` (default `b64_json`; `url` also supported)
- `COMET_MAX_RETRIES` (default `4`), `COMET_BACKOFF_BASE` (default `2.0` sec), `COMET_BACKOFF_CAP` (default `30.0` sec)
- `COMET_CONCURRENCY` (default `3`) — max parallel requests in a batch

### Core functions

- **`generate_comet(prompt, run_dir, filename, size, meta, client)`** — generates one image, saves it to `run_dir/filename`, and appends a JSONL record to `run_dir/_log.jsonl`. Accepts an optional shared `httpx.AsyncClient`; if omitted, creates and closes its own.
- **`generate_comet_batch(jobs, run_dir, concurrency, stop_on_error)`** — runs a list of `CometJob` entries concurrently under a semaphore, sharing one `httpx.AsyncClient`. Always returns a list aligned to `jobs`' order, with `Exception` objects in place of failed results (`return_exceptions=True` is always used internally, even when `stop_on_error=True`).
- **`CometJob`** (dataclass) — `prompt`, `filename`, `size` (default `1024x1024`), `meta` (free-form dict, logged verbatim).

### Key behaviors to preserve when modifying this module

- **Retry policy** (`_request_with_retry`): only retries HTTP 429 and 5xx (`_RETRYABLE_STATUS`), plus transport-level timeouts/errors. Other 4xx responses are returned as-is for the caller to handle — do not broaden this without reason. Honors a `Retry-After` response header when present, otherwise uses full-jitter exponential backoff (`_backoff_delay`).
- **Duplicate filename guard**: `generate_comet_batch` raises `ValueError` up front if two jobs share a `filename`, since a silent overwrite would lose a generated image in a series run.
- **`stop_on_error` semantics**: when `True`, a failure sets a shared `stop_flag` so not-yet-started jobs short-circuit with `asyncio.CancelledError` — but jobs already in flight or completed are never discarded. This exists specifically to avoid throwing away expensive, already-paid-for API results when one job in a batch fails.
- **Logging** (`_append_log`): every call (success or failure) appends one JSON line to `run_dir/_log.jsonl`, using synchronous append-only file I/O (deliberately not async — writes are short enough not to matter, and append-only is safe under concurrent callers).
- **Image decoding**: response handling supports both `b64_json` (decoded and written directly) and `url` (downloaded via the shared client) response formats, matching `COMET_RESPONSE_FORMAT`.

Comments and docstrings in this file are written in Korean; match that convention when editing `comet_4.py` unless asked otherwise.
