# Plan for Rollcall

## Open Tasks

## Completed Tasks

- [X] Transformed attendance tracker script into full Python application called `rollcall`
- [X] Created proper Python package structure under `src/rollcall/`
- [X] Updated `pyproject.toml` with proper package metadata and entry points
- [X] Split functionality into `core.py` (business logic) and `cli.py` (CLI interface)
- [X] Replaced argparse with Typer for modern CLI handling
- [X] Maintained all original command-line arguments (--session, --save-image, --no-terminal, --output)
- [X] Updated QUICKSTART.md to reflect new `uv run rollcall` command usage
- [X] Replaced README.md content with updated QUICKSTART.md for single source of truth
- [X] Verified application works correctly with `uv run rollcall --help` and test commands
- [X] Cleaned up old files (attendance.py, src/attendance_tracker/)
