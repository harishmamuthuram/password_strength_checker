# Password Strength Checker

A Python program that evaluates password strength using pattern 
checking and a common password blocklist.

## What it does
Checks a password against security requirements and a list of commonly 
used passwords, then returns a strength score and classification.

Requirements checked:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (!@#$%^&*?><)

Strength scoring:
- Weak: 0–2
- Medium: 3–4
- Strong: 5

## How to run
1. Clone the repo
2. Make sure common_passwords.txt is in the same folder
3. Run: python password_checker.py

## What I learned
Built this as a first step into understanding how password validation 
works and why common password blocklists matter in real authentication systems.
