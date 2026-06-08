# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a single-module Python library (`comet_4.py`) for async image generation via the Comet API (OpenAI-compatible). It is designed for batch series production—e.g., generating per-cut images for a storyboard—with retry logic, concurrency control, and append-only JSONL logging.

## No Build System or Test Framework

There is no `pyproject.toml`, `setup.py`, `Makefile`, or test suite. The sole dependency beyond the standard library is `httpx`. Install it with:

```bash
pip install httpx
```

To use the module in a script:

```python
import asyncio
from pathlib import Path
from comet_4 import generate_comet, generate_comet_batch, CometJob

asyncio.run(generate_comet("a red fox", run_dir=Path("out"), filename="fox.png"))
```

## Required Environment Variable

`COMET_API_KEY` must be set; the module raises `RuntimeError` immediately if it is missing.

All other config has defaults:

| Variable | Default |
|---|---|
| `COMET_BASE_URL` | `https://api.cometapi.com/v1` |
| `COMET_IMAGE_MODEL` | `flux-pro` |
| `COMET_TIMEOUT` | `180` (seconds) |
| `COMET_RESPONSE_FORMAT` | `b64_json` (`url` also supported) |
| `COMET_MAX_RETRIES` | `4` |
| `COMET_BACKOFF_BASE` | `2.0` |
| `COMET_BACKOFF_CAP` | `30.0` |
| `COMET_CONCURRENCY` | `3` |

## Architecture

**Public API:**
- `generate_comet(prompt, run_dir, filename, size, meta, client)` — generates one image and writes it to `run_dir/filename`. Accepts an optional shared `httpx.AsyncClient`; if none is provided it creates and closes its own.
- `generate_comet_batch(jobs, run_dir, concurrency, stop_on_error)` — takes an `Iterable[CometJob]` and runs all jobs in parallel under a `asyncio.Semaphore`. Always uses `asyncio.gather(return_exceptions=True)` so completed results are never lost.
- `CometJob` — dataclass with `prompt`, `filename`, `size` (default `"1024x1024"`), and `meta` (free dict stored in the log).

**Retry layer (`_request_with_retry`):** retries only on `{429, 500, 502, 503, 504}` and on `httpx.TimeoutException`/`httpx.TransportError`. Respects `Retry-After` headers; otherwise uses full-jitter exponential backoff.

**Logging:** every call (success or failure) appends one JSON line to `run_dir/_log.jsonl`. `_append_log` uses synchronous file I/O (short append) intentionally—it does not block the event loop meaningfully and avoids async file-handle complexity.

**`stop_on_error` semantics:** when `True`, a `stop_flag` (`asyncio.Event`) is set on the first exception. Jobs that haven't acquired the semaphore yet raise `asyncio.CancelledError` and are skipped. Already-running or completed jobs are unaffected—their results appear normally in the returned list.

**Duplicate filename guard:** `generate_comet_batch` raises `ValueError` before any API call if two `CometJob` entries share the same `filename`, preventing silent overwrites in series production.
