import random
import string


def generate_password(length, lowercase=True, uppercase=True, digits=True, punctuation=False):
    """
    Generates a random password based on user input.

    Args:
        length (int): Desired length of the password.
        lowercase (bool, optional): Include lowercase letters (default: True).
        uppercase (bool, optional): Include uppercase letters (default: True).
        digits (bool, optional): Include digits (default: True).
        punctuation (bool, optional): Include punctuation marks (default: False).

    Returns:
        str: The generated random password.
    """

    # Define character sets based on user preferences
    characters = ""
    if lowercase:
        characters += string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    # Check if any character sets are selected
    if not characters:
        raise ValueError("Please select at least one character type (lowercase, uppercase, digits, punctuation).")

    # Generate random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password


# Get user input for password length
while True:
    try:
        length = int(input("Enter desired password length (minimum 8 characters): "))
        if length < 8:
            print("Password length must be at least 8 characters. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Get user input for complexity (optional)
complexity_options = {
    "1": (True, True, True, False),
    "2": (True, True, True, True),
}
print("\nComplexity Options:")
print("1. Lowercase, Uppercase, Digits")
print("2. Lowercase, Uppercase, Digits, Punctuation")
complexity_choice = input("Choose complexity (default: 1): ") or "1"

if complexity_choice not in complexity_options:
    print("Invalid choice. Using default complexity (option 1).")
    complexity = complexity_options["1"]
else:
    complexity = complexity_options[complexity_choice]

# Generate password and display
password = generate_password(length, *complexity)
print(f"\nYour generated password is: {password}")
