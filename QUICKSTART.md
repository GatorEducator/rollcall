# Quick Start Guide - WORKING VERSION

## ✅ Verified Working Setup

### Step 1: Create Your Google Form

1. Go to https://forms.google.com
2. Click "Blank form"
3. Title: "Class Attendance"
4. Add these questions **in this exact order**:

**Question 1:**
- Question: "Date"
- Type: Short answer
- Required: Yes

**Question 2:**
- Question: "Time"  
- Type: Short answer
- Required: Yes

**Question 3:**
- Question: "Date and Time"
- Type: Short answer
- Required: Yes

**Question 4:**
- Question: "Session"
- Type: Short answer
- Required: Yes

**Question 5:**
- Question: "Your Name"
- Type: Short answer
- Required: Yes

**Question 6:**
- Question: "Your Email"
- Type: Short answer
- Required: Yes

### Step 2: Get Full Form URL and Entry IDs

**⚠️ CRITICAL**: You must use the FULL URL format, not forms.gle short URLs!

1. Click "Send" button (top right)
2. Click the link icon 🔗
3. **Copy the FULL URL** - it looks like:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdj93F7_7xUiHzvwE_BHJg1m8o1uSNSZVf79J2oYaKoGdCP5A/viewform
   ```
   **Save this URL - you'll use it with the program!**

4. Click "Get pre-filled link"
5. Fill in sample data for the first 4 fields only:
   - Date: "2025-01-01"
   - Time: "10:00:00"  
   - Date and Time: "2025-01-01 10:00:00"
   - Session: "Sample Class"
   - **Leave Name and Email blank**
6. Click "Get link"
7. Copy the URL with parameters - it will look like:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdj93F7_7xUiHzvwE_BHJg1m8o1uSNSZVf79J2oYaKoGdCP5A/viewform?usp=pp_url&entry.275116116=2025-01-01&entry.1240679346=10:00:00&entry.413810672=2025-01-01+10:00:00&entry.850922479=Sample+Class
   ```

### Step 3: Extract Your Entry IDs

From the pre-filled URL above, identify your entry IDs:
- `entry.275116116` - Date field
- `entry.1240679346` - Time field
- `entry.413810672` - Date/Time field  
- `entry.850922479` - Session field

**Your entry IDs will be different!** Write them down.

### Step 4: Update the Python Program

1. Open `src/attendance_tracker/main.py`
2. Find this section (around line 35):
   ```python
   prefill_params = {
       'entry.275116116': date_str,     # Date field
       'entry.1240679346': time_str,    # Time field
       'entry.413810672': datetime_str, # DateTime field
       'entry.850922479': session_name, # Session field
   }
   ```

3. Replace the entry IDs with YOUR actual ones from step 3:
   ```python
   prefill_params = {
       'entry.YOUR_DATE_ID': date_str,     # Replace with your Date entry ID
       'entry.YOUR_TIME_ID': time_str,     # Replace with your Time entry ID
       'entry.YOUR_DATETIME_ID': datetime_str, # Replace with your DateTime entry ID
       'entry.YOUR_SESSION_ID': session_name,  # Replace with your Session entry ID
   }
   ```

### Step 5: Test the Program

**Use the FULL URL from Step 2, not the pre-filled URL!**

```bash
# Test with your full form URL
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"

# Example with the working test form:
uv run python attendance.py "https://docs.google.com/forms/d/e/1FAIpQLSdj93F7_7xUiHzvwE_BHJg1m8o1uSNSZVf79J2oYaKoGdCP5A/viewform" --session "Test Class"
```

### Step 6: Verify It Works

1. Run the program and copy the generated URL
2. Paste the URL into your browser
3. Verify the form opens with date/time/session pre-filled
4. Complete name and email fields  
5. Submit and check that the response appears in Google Forms

### ✅ Working Example Commands

```bash
# Generate QR for today's class
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform" --session "Document Engineering - Week 5"

# Save as image for projection
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform" --session "Math 101" --save-image --output "math101_attendance.png"

# Generate without terminal display (for scripts)
uv run python attendance.py "https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform" --no-terminal --save-image
```

## ⚠️ Common Issues and Solutions

### "Dynamic Link Not Found" Error
- **Cause**: Using forms.gle short URL instead of full URL
- **Solution**: Use the full `https://docs.google.com/forms/d/e/...` URL format

### Form Opens But Fields Aren't Pre-filled
- **Cause**: Wrong entry IDs in the code
- **Solution**: Double-check entry IDs from your pre-filled URL and update the code

### Program Shows Warning About forms.gle
- **Cause**: Using short URL format
- **Solution**: Switch to full URL format as shown in Step 2

**That's it!** Students scan the QR code → form opens with date/time/session pre-filled → they add name/email → submit → done!
