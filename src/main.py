import re 
import json
import os

email_pattern = r"[a-zA-Z0-9]+@(?:(?:alumni\.|si\.)?alueducation|alustudent)\.com"
phone_number_pattern = r"(?:\+250|0)?7(?:8|9)\s?[0-9]{3}\s?[0-9]{4}"
url_pattern = r"https:\/\/(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:\/[^\s]*)?"
card_pattern = r"4[0-9]{12}(?:[0-9]{3})?"

with open("input/raw-text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

results = {
    "valid_emails" : re.findall(email_pattern, raw_text, re.MULTILINE),
    "urls" : re.findall(url_pattern, raw_text, re.MULTILINE),
    "phone_numbers": re.findall(phone_number_pattern, raw_text, re.MULTILINE),
    "bank_cards": re.findall(card_pattern, raw_text, re.MULTILINE) 
}

with open ("output/sample-output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Extraction complete. Results saved to output/sample-output.json")
print(json.dumps(results, indent=2))