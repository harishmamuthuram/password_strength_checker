# Password Strength Checker

A beginner-friendly Python program to check the strength of a password.  

## Features
- Checks if the password is in a list of **common passwords**.
- Ensures the password meets security requirements:
  - At least **8 characters long**
  - Contains at least **one uppercase letter**
  - Contains at least **one lowercase letter**
  - Contains at least **one number**
  - Contains at least **one special character** (`! @ # $ % ^ & * ? > <`)
- Provides a **password strength score** (0–5) and classification:
  - Weak (0–2)
  - Medium (3–4)
  - Strong (5)

## How to use
1. Clone this repository.
2. Make sure there is a `common_passwords.txt` file in the same folder. This file should contain commonly used passwords, one per line.
3. Run the script:

```bash
python password_checker.py
