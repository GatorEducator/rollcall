"""Core functionality of the rollcall program that generates a QR Code for attendance tracking."""

import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs
import qrcode
import qrcode.constants


def load_config(config_path: Path) -> dict:
    """Load configuration from JSON file."""
    try:
        with config_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in configuration file: {e}")


def get_class_config(config: dict, class_name: str) -> dict:
    """Get configuration for a specific class."""
    if class_name not in config:
        raise ValueError(f"Class '{class_name}' not found in configuration")
    class_config = config[class_name]
    if "form_url" not in class_config or "prefill_params" not in class_config:
        raise ValueError(
            f"Invalid configuration for class '{class_name}': missing form_url or prefill_params"
        )
    return class_config


def generate_attendance_url(
    base_form_url: str, session_name: str, prefill_params: dict[str, str]
) -> str:
    """Generate attendance URL with pre-filled form parameters."""
    current_time = datetime.now()
    date_str = current_time.strftime("%Y-%m-%d")
    time_str = current_time.strftime("%H:%M:%S")
    datetime_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # warn user if they're using a short URL
    if "forms.gle" in base_form_url:
        print("⚠️  WARNING: You're using a forms.gle short URL.")
        print("   For best results, convert to the full URL format:")
        print("   1. Open your form")
        print("   2. Click 'Send' → Link icon")
        print("   3. Copy the full URL (starts with https://docs.google.com/forms)")
        print("   4. Use that URL instead")
        print()
    # parse the URL to extract form ID and existing parameters
    parsed_url = urlparse(base_form_url)
    # build prefill parameters from config
    params = {
        prefill_params["date_field"]: date_str,
        prefill_params["time_field"]: time_str,
        prefill_params["datetime_field"]: datetime_str,
        prefill_params["session_name_field"]: session_name,
    }
    # if the URL already has parameters, preserve them
    if parsed_url.query:
        existing_params = parse_qs(parsed_url.query, keep_blank_values=True)
        # flatten the existing parameters (parse_qs returns lists)
        for key, value_list in existing_params.items():
            if value_list:
                params[key] = value_list[0]
    # build the complete URL with pre-filled parameters
    query_string = urlencode(params)
    # handle different Google Forms URL formats
    if "docs.google.com/forms" in base_form_url:
        # full URL format - ensure it has /viewform
        if "/viewform" not in base_form_url:
            if base_form_url.endswith("/"):
                attendance_url = f"{base_form_url}viewform?{query_string}"
            else:
                attendance_url = f"{base_form_url}/viewform?{query_string}"
        else:
            base_without_query = base_form_url.split("?")[0]
            attendance_url = f"{base_without_query}?{query_string}"
    else:
        # handle forms.gle or other formats - just add query parameters
        if "?" in base_form_url:
            attendance_url = f"{base_form_url}&{query_string}"
        else:
            attendance_url = f"{base_form_url}?{query_string}"
    return attendance_url


def generate_qr_code(data: str, display_in_terminal: bool = True) -> qrcode.QRCode:
    """Generate QR code for the given data."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    if display_in_terminal:
        # display QR code in terminal using ASCII characters
        qr_ascii = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=2,
        )
        qr_ascii.add_data(data)
        qr_ascii.make(fit=True)
        qr_ascii.print_ascii(invert=True)
    return qr


def save_qr_code_image(qr: qrcode.QRCode, filename: str = "attendance_qr.png") -> None:
    """Save QR code as an image file."""
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as: {filename}")
