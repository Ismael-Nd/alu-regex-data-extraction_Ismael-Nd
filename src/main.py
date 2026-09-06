import re 
import json

## This regex matches ALU staff and optional student addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@(?:(?:alumni\.|si\.)?alueducation|alustudent)\.com"

# The regex matches rwandan mobile numbers startinf with 078 or 079 
# with an otional prefix of +250 or a 0. It also allows optional 
# spaces between digit groups to handle real world digits, and last grouping of {3,4} 
# beacuse rwandan digits can be grouped by 3 or 4 digits 
phone_number_pattern = r"(?:\+250|0)?7(?:8|9)\s?[0-9]{3}\s?[0-9]{3,4}"

# The URL matches http and https with or without "www" with an optional path query or string after the domain 
url_pattern = r"https:\/\/(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:\/[^\s]*)?"

# This regex matches visa style card numbers that starts with 4 and has 12 or 13 digits 
card_pattern = r"4[0-9]{12}(?:[0-9]{3})?"

## Security Integrity ##

def mask_card(card_number): 
    # Masks all but at least 4 digit if a credit card number
    # before it is stored or displayed 
    return "*" * (len(card_number) - 4) + card_number[-4:]

def is_safe_length(text, max_length=100000):
    # Basic defence check for rejecting very large input 
    # before runnig regex against it
    return len(text) <= max_length

## THE EXTRACTION LOGIC ##

with open("input/raw-text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

if not is_safe_length(raw_text):
    raise ValueError("The input text is too long for processing")

# Any present script text in here is prossed as plain text data
# so it is never executed y the program
results = {
    "valid_emails" : re.findall(email_pattern, raw_text, re.MULTILINE),
    "urls" : re.findall(url_pattern, raw_text, re.MULTILINE),
    "phone_numbers": re.findall(phone_number_pattern, raw_text, re.MULTILINE),
    "bank_cards": [mask_card(c) for c in re.findall(card_pattern, raw_text)],
}

with open ("output/sample-output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Extraction complete. Results saved to output/sample-output.json")
print(json.dumps(results, indent=2))