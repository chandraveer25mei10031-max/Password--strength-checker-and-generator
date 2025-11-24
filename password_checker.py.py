import secrets
import string
import random

# Function to generate a secure password with complexity rules
def generate_secure_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8")
    chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    password += [secrets.choice(chars) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

# Function to check password strength
def check_password_strength(password):
    length_ok = len(password) >= 8
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    score = sum([length_ok, lower, upper, digit, special])

    remarks = []
    if not length_ok:
        remarks.append("Password should be at least 8 characters.")
    if not lower:
        remarks.append("Add lowercase letters.")
    if not upper:
        remarks.append("Add uppercase letters.")
    if not digit:
        remarks.append("Add digits.")
    if not special:
        remarks.append("Add special characters (e.g. !@#%).")

    if score == 5 and len(password) >= 12:
        strength = "Very Strong"
    elif score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print("\n--- Password Analysis ---")
    print(f"Password: {password}")
    print(f"Strength: {strength}")
    if remarks:
        print("Recommendations:")
        for r in remarks:
            print(f"- {r}")
    else:
        print("All requirements met!")

# Main interaction loop
def main():
    while True:
        print("\n--- Password Strength Checker & Generator ---")
        print("1. Check Password Strength")
        print("2. Generate Secure Password")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            password = input("Enter your password: ")
            check_password_strength(password)
        elif choice == '2':
            try:
                length = int(input("Enter desired password length (min 8): "))
                pw = generate_secure_password(length)
                print(f"Generated Secure Password: {pw}")
            except Exception as e:
                print("Error:", e)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid selection, try again.")

if __name__ == '__main__':
    main()
