"""Test cases for core.py functions."""

import json
from pathlib import Path

import pytest

from rollcall.core import load_config


def test_load_config_success(tmp_path: Path) -> None:
    """Test successful loading of valid JSON configuration."""
    config_data = {
        "class1": {
            "form_url": "https://example.com",
            "prefill_params": {"date_field": "entry.1"},
        }
    }
    config_file = tmp_path / "config.json"
    with config_file.open("w") as f:
        json.dump(config_data, f)
    result = load_config(config_file)
    assert result == config_data


def test_load_config_file_not_found() -> None:
    """Test FileNotFoundError when configuration file does not exist."""
    with pytest.raises(
        FileNotFoundError, match="Configuration file not found"
    ):
        load_config(Path("nonexistent.json"))


def test_load_config_invalid_json(tmp_path: Path) -> None:
    """Test ValueError when configuration file contains invalid JSON."""
    config_file = tmp_path / "invalid.json"
    config_file.write_text("{invalid json")
    with pytest.raises(ValueError, match="Invalid JSON in configuration file"):
        load_config(config_file)
