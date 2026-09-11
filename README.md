# Regex Data Extraction Tool

## This is a python program extracts and validates structured information from realistic raw text using regula expressions.

## Data extracted 

- ALU email adress
- URLs
- Rwandan phone numbers
- Visa-style credit credit card numbers 

## ALU Email Validation 

- @alueducation.com
- @alumni.alueducation.com
- @si.alueducation.com

Other emails are ignored. 

## Security 

The program treats all input untrusted.

It detects suspicious patterns such as scripts tags and injection-like content. Sensitive inforamtion such as email and credit card numbers is masked before being writtern to output.

The program also rejects excessively large input files.

## Run 

From the root directory:

python src/main.py

## Input 

input/raw-text.txt

## Output 

output/sample-output.json