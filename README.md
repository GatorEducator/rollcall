# Rollcall

A Python program that generates QR codes linking to Google Forms with pre-filled
attendance information including date, time, and session details.

## Features

- ✅ Automatically generates QR codes for attendance tracking
- ✅ Pre-fills Google Form with current date, time, and session information
- ✅ Displays QR codes in terminal using ASCII characters
- ✅ Optionally saves QR codes as PNG image files
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

1. Clone or download the attendance-tracker directory
2. Navigate to the project directory:
   ```bash
   cd attendance-tracker
   ```
3. Install dependencies (automatically creates virtual environment):
   ```bash
   uv sync
   ```

## Google Form Setup

### Step 1: Create a Google Form

1. Go to [forms.google.com](https://forms.google.com)
2. Create a new form titled "Class Attendance"
3. Add the following fields (in this exact order):

#### Required Form Fields:

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

### Step 2: Get Pre-fill URLs and Extract Entry IDs

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

### Step 3: Extract Entry IDs

From your pre-filled URL, note the entry IDs:
- `entry.123456789` - Date field
- `entry.234567890` - Time field  
- `entry.345678901` - Date/Time field
- `entry.456789012` - Session field

### Step 4: Update the Program

Edit `src/attendance_tracker/main.py` and replace the placeholder entry IDs (around line 35):

```python
# Replace these with your actual entry IDs from step 3
prefill_params = {
    'entry.123456789': date_str,        # Your Date field entry ID
    'entry.234567890': time_str,        # Your Time field entry ID  
    'entry.345678901': datetime_str,    # Your Date/Time field entry ID
    'entry.456789012': session_name,    # Your Session field entry ID
}
```

**Example**: If your entry IDs are 275116116, 1240679346, 413810672, and 850922479, update the code to:

```python
prefill_params = {
    'entry.275116116': date_str,        # Date field
    'entry.1240679346': time_str,       # Time field  
    'entry.413810672': datetime_str,    # Date/Time field
    'entry.850922479': session_name,    # Session field
}
```

## Usage

### Basic Usage

```bash
# Display QR code in terminal (use the FULL URL, not forms.gle short URL)
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"

# Specify session name
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform" --session "Math 101"

# Save QR code as image file
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform" --save-image

# Save with custom filename
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform" --save-image --output "math101_qr.png"

# Don't display in terminal (useful for automated scripts)
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform" --no-terminal --save-image
```

### ⚠️ Important Notes

1. **Use FULL URLs**: Always use the full `https://docs.google.com/forms/d/e/...` URL format, not `forms.gle` short URLs
2. **Update Entry IDs**: Make sure you've updated the entry IDs in the source code with your actual form's entry IDs
3. **Test First**: Test the generated URL manually in a browser to ensure it works before using with students

### Command Line Options

- `form_url`: Your Google Form URL (required - must be full URL format)
- `--session SESSION`: Session/class name (default: "Class")
- `--save-image`: Save QR code as PNG image file
- `--no-terminal`: Don't display QR code in terminal
- `--output FILENAME`: Output filename for image (default: "attendance_qr.png")

### Example Workflow

1. **Before class**: Run the program to generate a QR code:
   ```bash
   uv run python attendance.py "https://docs.google.com/forms/d/e/1FAIpQLSdj93F7_7xUiHzvwE_BHJg1m8o1uSNSZVf79J2oYaKoGdCP5A/viewform" --session "Document Engineering - Week 1" --save-image
   ```

2. **During class**: Display the QR code on your screen or projector

3. **Students**: Scan the QR code with their phones, which opens the pre-filled form

4. **Students**: Complete the remaining fields (name, email) and submit

5. **After class**: View responses in Google Forms or export to Google Sheets

## How It Works

1. **QR Code Generation**: Creates a QR code containing a URL to your Google Form
2. **Pre-filling**: Automatically appends current date, time, and session info to the form URL
3. **Student Experience**: Students scan → form opens → date/time/session already filled → they add name/email → submit
4. **Data Collection**: All responses saved to Google Forms/Sheets with timestamp verification

## Troubleshooting

### Common Issues

1. **"qrcode library not found"**
   - Run: `uv sync` to install dependencies

2. **Entry IDs not working**
   - Double-check you copied the correct entry IDs from your pre-filled URL
   - Make sure the form fields are in the correct order

3. **QR code not displaying properly**
   - Try using `--save-image` and view the PNG file
   - Some terminals may not display ASCII QR codes clearly

4. **Students can't access form**
   - Make sure your Google Form is set to "Anyone with the link"
   - Test the generated URL manually in a browser

### Testing

Test your setup by:
1. Running the program with your form URL
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
