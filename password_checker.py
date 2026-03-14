divider = "------------------------------------------------------------\n"
print(divider)
print("PASSWORD STRENGTH CHECKER\n")
print("- Your password must be at least 8 characters long.")
print("- It must contain at least one uppercase letter, one lowercase letter, one number, and one special character.")
print("- Avoid using common passwords to ensure maximum security.\n")
print(divider)

# ------------------ Load common passwords ------------------
# Open the file 'common_passwords.txt' and store each password in a list
# Strip newline characters and extra spaces

common_passwords_list=[]
f=open("common_passwords.txt", "r")
for line in f:
    stripped_password = line.strip()
    common_passwords_list.append(stripped_password)

f.close()

# ------------------ User Input ------------------
# Ask the user to enter their password
password=input("Please enter the password: ")


if password.lower() in [p.lower() for p in common_passwords_list]:
    print("Very weak password. Please try again.")
    exit()
    

has_upper = has_lower = has_digit = has_special = False
special_characters = {'!','@','#','$','%','^','&','*','?','>','<'}

for i in password:
    if i.isupper():
        has_upper = True
    if i.islower():
        has_lower = True
    if i.isdigit():
        has_digit = True
    if i in special_characters:
        has_special = True

score = 0
if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1
    
print(f"Your password score is: {score}/5")

if score in range(0, 3):   
    print("Your password is weak. Please create a stronger password for optimum security.")
elif score in range(3, 5):
    print("Your password is medium. It would be advised to create a more stronger password for optimum security.")
elif score == 5:
    print("Your password is strong. You may proceed with using this password.")




