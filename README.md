# password-strength-checker

A Python tool that evaluates password strength using pattern checking and a common password blocklist — returns a score and classification.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Type](https://img.shields.io/badge/tool-password--validation-green)

---

## Features
- Checks against 5 security requirements
- Cross-references a `common_passwords.txt` blocklist
- Returns a score (0–5) and a Weak / Medium / Strong classification

---

## Requirements checked

| Rule | Requirement |
|------|------------|
| Length | Minimum 8 characters |
| Uppercase | At least one A–Z |
| Lowercase | At least one a–z |
| Number | At least one 0–9 |
| Special char | At least one of `!@#$%^&*?><` |

---

## Scoring

- **Weak** — 0 to 2 requirements met
- **Medium** — 3 to 4 requirements met
- **Strong** — all 5 requirements met

---

## Usage

```bash
password_checker.py
```

Make sure `common_passwords.txt` is in the same folder before running.

---

## Built as part of

Built to understand why password validation and common password blocklists matter in real authentication systems.
