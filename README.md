# Rollcall

A Python program that generates QR codes linking to Google Forms with pre-filled
attendance information including date, time, and session details. Now configurable
via JSON for multiple classes.

## Features

- ✅ Automatically generates QR codes for attendance tracking
- ✅ Pre-fills Google Form with current date, time, and session information
- ✅ Displays QR codes in terminal using ASCII characters
- ✅ Optionally saves QR codes as PNG image files
- ✅ Configurable via JSON for multiple classes and forms
- ✅ Cross-platform compatibility (Linux, macOS, Windows)
- ✅ Managed with UV for easy dependency management
- ✅ Uses Python 3.13 with minimal dependencies

## Installation

### Prerequisites

1. **UV Package Manager**: Install from [astral-sh.github.io/uv](https://astral-sh.github.io/uv/)
   - Unix/macOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

2. **Python 3.13**: Will be automatically installed by UV if not present

### Setup

1. Clone or download the rollcall directory
2. Navigate to the project directory:
   ```bash
   cd rollcall
   ```
3. Install dependencies (automatically creates virtual environment):
   ```bash
   uv sync
   ```

## Configuration

### Step 1: Create rollcall.json

Create a `rollcall.json` file in your project directory with your class configurations:

```json
{
    "Computer Science 101": {
        "form_url": "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform",
        "prefill_params": {
            "date_field": "entry.YOUR_DATE_ENTRY_ID",
            "time_field": "entry.YOUR_TIME_ENTRY_ID",
            "datetime_field": "entry.YOUR_DATETIME_ENTRY_ID",
            "session_name_field": "entry.YOUR_SESSION_ENTRY_ID"
        }
    },
    "Math 101": {
        "form_url": "https://docs.google.com/forms/d/e/ANOTHER_FORM_ID/viewform",
        "prefill_params": {
            "date_field": "entry.ANOTHER_DATE_ID",
            "time_field": "entry.ANOTHER_TIME_ID",
            "datetime_field": "entry.ANOTHER_DATETIME_ID",
            "session_name_field": "entry.ANOTHER_SESSION_ID"
        }
    }
}
```

### Step 2: Google Form Setup

#### Create a Google Form

1. Go to [forms.google.com](https://forms.google.com)
2. Create a new form titled "Class Attendance"
3. Add the following fields (in this exact order):

##### Required Form Fields:

1. **Date Field**
   - Question: "Date"
   - Type: Short answer
   - Make required: Yes

2. **Time Field**
   - Question: "Time"
   - Type: Short answer
   - Make required: Yes

3. **Date/Time Field**
   - Question: "Date and Time"
   - Type: Short answer
   - Make required: Yes

4. **Session/Class Field**
   - Question: "Session"
   - Type: Short answer
   - Make required: Yes

5. **Student Name Field**
   - Question: "Your Name"
   - Type: Short answer
   - Make required: Yes

6. **Student Email Field**
   - Question: "Your Email"
   - Type: Short answer
   - Make required: Yes

#### Get Pre-fill URLs and Extract Entry IDs

**IMPORTANT**: You must use the full Google Forms URL format (not forms.gle short URLs) for the program to work correctly.

1. In your Google Form, click the **Send** button (top right)
2. Click the **link icon** (🔗)
3. **Copy the full URL** - it should look like:
   ```
   https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform
   ```
4. Click **"Get pre-filled link"** at the bottom
5. Fill in sample data for the first 4 fields:
   - Date: "2025-01-01"
   - Time: "10:00:00"
   - Date and Time: "2025-01-01 10:00:00"
   - Session: "Sample Class"
6. Click **"Get link"**
7. Copy the generated pre-filled URL - it will look like:
   ```
   https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?usp=pp_url&entry.123456789=2025-01-01&entry.234567890=10:00:00&entry.345678901=2025-01-01+10:00:00&entry.456789012=Sample+Class
   ```

#### Extract Entry IDs

From your pre-filled URL, note the entry IDs:
- `entry.123456789` - Date field
- `entry.234567890` - Time field
- `entry.345678901` - Date/Time field
- `entry.456789012` - Session field

Update your `rollcall.json` with these entry IDs.

## Usage

### Basic Usage

```bash
# Display QR code in terminal for a class
uv run rollcall "Computer Science 101"

# Specify session name
uv run rollcall "Computer Science 101" --session "Math 101 - Lecture 1"

# Save QR code as image file
uv run rollcall "Computer Science 101" --save-image

# Save with custom filename
uv run rollcall "Computer Science 101" --save-image --output "cs101_qr.png"

# Use custom config file
uv run rollcall "Computer Science 101" --config /path/to/my/rollcall.json

# Don't display in terminal (useful for automated scripts)
uv run rollcall "Computer Science 101" --no-terminal --save-image
```

### ⚠️ Important Notes

1. **Use FULL URLs**: Always use the full `https://docs.google.com/forms/d/e/...` URL format in your JSON, not `forms.gle` short URLs
2. **Update Entry IDs**: Make sure you've updated the entry IDs in your `rollcall.json` with your actual form's entry IDs
3. **Test First**: Test the generated URL manually in a browser to ensure it works before using with students

### Command Line Options

- `class_name`: Name of the class (required - must match a key in rollcall.json)
- `--config CONFIG`: Path to rollcall.json (default: "rollcall.json")
- `--session SESSION`: Session/class name (default: "Class")
- `--save-image`: Save QR code as PNG image file
- `--no-terminal`: Don't display QR code in terminal
- `--output FILENAME`: Output filename for image (default: "attendance_qr.png")

### Example Workflow

1. **Before class**: Run the program to generate a QR code:
   ```bash
   uv run rollcall "Computer Science 101" --session "Document Engineering - Week 1" --save-image
   ```

2. **During class**: Display the QR code on your screen or projector

3. **Students**: Scan the QR code with their phones, which opens the pre-filled form

4. **Students**: Complete the remaining fields (name, email) and submit

5. **After class**: View responses in Google Forms or export to Google Sheets

## How It Works

1. **Configuration Loading**: Reads class settings from rollcall.json
2. **QR Code Generation**: Creates a QR code containing a URL to your Google Form
3. **Pre-filling**: Automatically appends current date, time, and session info to the form URL
4. **Student Experience**: Students scan → form opens → date/time/session already filled → they add name/email → submit
5. **Data Collection**: All responses saved to Google Forms/Sheets with timestamp verification

## Troubleshooting

### Common Issues

1. **"Configuration file not found"**
   - Ensure rollcall.json exists in the current directory or specify path with --config

2. **"Class not found in configuration"**
   - Check that the class name matches exactly (case-sensitive) a key in rollcall.json

3. **Entry IDs not working**
   - Double-check you copied the correct entry IDs from your pre-filled URL
   - Make sure the form fields are in the correct order

4. **QR code not displaying properly**
   - Try using `--save-image` and view the PNG file
   - Some terminals may not display ASCII QR codes clearly

5. **Students can't access form**
   - Make sure your Google Form is set to "Anyone with the link"
   - Test the generated URL manually in a browser

### Testing

Test your setup by:
1. Running the program with your class name
2. Scanning the QR code with your phone
3. Verifying the form opens with pre-filled date/time/session data
4. Submitting a test response
5. Checking that the response appears in your Google Form responses

## Security Considerations

- The QR codes contain the current date/time, making them session-specific
- Students still need to provide their name and email manually
- Form responses include timestamps for verification
- Consider setting your Google Form to require sign-in for additional verification

## Dependencies

- **qrcode**: QR code generation (installed via UV)
- **pillow**: Image processing for QR codes (installed via UV)
- **Python 3.13**: Core runtime (managed by UV)

All dependencies are automatically managed by UV package manager.
