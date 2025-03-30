print("This is 07-Password-Generator-Python-Project")

import random
import string

# Function to generate a password
def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special_chars = "!@#$%^&*()" if use_special_chars else ""

    # Combine all character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        return "❌ Error: Please select at least one character set."

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Function to check password strength
def check_password_strength(password):
    strength = 0
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()" for char in password):
        strength += 1
    if len(password) >= 12:
        strength += 1

    if strength == 5:
        return "💪 Strong"
    elif strength >= 3:
        return "👍 Medium"
    else:
        return "👎 Weak"

# Main function to run the password generator
def main():
    print("Welcome to the Password Generator! 🔐")

    # Get password length from the user
    try:
        length = int(input("Enter the length of the password minimum (e.g., 12): "))
        if length <= 0:
            print("❌ Error: Password length must be greater than 0.")
            return
    except ValueError:
        print("❌ Error: Please enter a valid number.")
        return

    # Get user preferences
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    # Display the generated password and its strength
    print("\n🔑 Your Generated Password:")
    print(f"📜 {password}")
    print(f"🔒 Password Strength: {check_password_strength(password)}")

# Run the program
if __name__ == "__main__":
    main()