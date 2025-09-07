"""Rollcall CLI - Command Line Interface using Typer."""

from datetime import datetime

import typer
from typing_extensions import Annotated

from .core import generate_attendance_url, generate_qr_code, save_qr_code_image

app = typer.Typer(
    name="rollcall",
    help="Generate QR codes for class attendance tracking",
    add_completion=False,
)


@app.command()
def main(
    form_url: Annotated[
        str, typer.Argument(help="Google Form URL for attendance tracking")
    ],
    session: Annotated[
        str, typer.Option("--session", help="Session/class name")
    ] = "Class",
    save_image: Annotated[
        bool, typer.Option("--save-image", help="Save QR code as PNG image file")
    ] = False,
    no_terminal: Annotated[
        bool, typer.Option("--no-terminal", help="Don't display QR code in terminal")
    ] = False,
    output: Annotated[
        str, typer.Option("--output", help="Output filename for QR code image")
    ] = "attendance_qr.png",
) -> None:
    """Generate QR codes for class attendance tracking with pre-filled form data."""
    try:
        # generate the attendance URL with current date/time
        attendance_url = generate_attendance_url(form_url, session)
        typer.echo(f"Generating QR code for session: {session}")
        typer.echo(f"Current date/time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        typer.echo(f"Form URL: {attendance_url}")
        typer.echo("")
        # generate and display QR code
        qr = generate_qr_code(attendance_url, display_in_terminal=not no_terminal)
        if save_image:
            save_qr_code_image(qr, output)
        typer.echo("")
        typer.echo("Students can scan this QR code to mark their attendance.")
        typer.echo(
            "The form will be automatically pre-filled with today's date and time."
        )
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
