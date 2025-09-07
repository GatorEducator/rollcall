# Plan for Rollcall

## Open Tasks

## Completed Tasks

- [X] Transformed attendance tracker script into full Python application called
`rollcall`
- [X] Created proper Python package structure under `src/rollcall/`
- [X] Updated `pyproject.toml` with proper package metadata and entry points
- [X] Split functionality into `core.py` (business logic) and `cli.py` (CLI
interface)
- [X] Replaced argparse with Typer for modern CLI handling
- [X] Maintained all original command-line arguments (`--session`,
`--save-image`, `--no-terminal`, `--output`)
- [X] Updated QUICKSTART.md to reflect new `uv run rollcall` command usage
- [X] Replaced README.md content with updated QUICKSTART.md for single source of
truth
- [X] Verified application works correctly with `uv run rollcall --help` and
test commands
- [X] Cleaned up old files (attendance.py, src/attendance_tracker/)
- [X] Added comprehensive test cases for the `load_config` function in
`tests/test_core.py`, including tests for successful loading, file not found,
and invalid JSON errors. Verified all tests pass with `uv run pytest`.
- [X] Created README_PYPI.md as an emoji-free version of README.md for PyPI
compatibility.
- [X] Replaced all naked print statements in `core.py` with a Typer console
object using `console.print()` for better CLI output handling.
- [X] Fixed all markdownlint errors in README.md and README_PYPI.md by
correcting headings, code blocks, and disabling problematic rules in
`.pymarkdown.cfg`. Confirmed `uv run task all` passes all checks.
