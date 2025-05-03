import re
import requests

# Step 1: Download the raw file
url = "https://raw.githubusercontent.com/eneko/Pi/master/one-million.txt"
response = requests.get(url)
raw_text = response.text

# Step 2: Strip everything before the digits
# This matches from the first "3." and skips it (removes the '3.')
raw_digits = re.sub(r".*?3\.", "", raw_text, flags=re.DOTALL)

# Step 3: Remove all non-digit characters (spaces, newlines, etc.)
pi_digits = ''.join(filter(str.isdigit, raw_digits))

# Optional: sanity check
print("Digit count:", len(pi_digits))  # Should be 1_000_000

# Step 4: Save to cleaned file
with open("pi_1mil_clean.txt", "w") as f:
    f.write(pi_digits)
