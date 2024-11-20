# Function to validate password based on selected criteria
def validate_password(password, criteria):
    if len(password) < 8:
        print(f'"{password}" is Invalid. Less than 8 Characters.')
        return False

    # Checking criteria
    if 1 in criteria and not any(char.isupper() for char in password):
        print(f'"{password}" is Invalid. Missing Uppercase letters.')
        return False
    if 2 in criteria and not any(char.islower() for char in password):
        print(f'"{password}" is Invalid. Missing Lowercase letters.')
        return False
    if 3 in criteria and not any(char.isdigit() for char in password):
        print(f'"{password}" is Invalid. Missing Numbers.')
        return False
    if 4 in criteria and not any(char in "!@#" for char in password):
        print(f'"{password}" is Invalid. Missing Special characters (!, @, #).')
        return False
    if any(char == '$' for char in password):
        print(f'"{password}" is Invalid. It contains $ which is not allowed.')
        return False

    print(f'"{password}" is Valid.')
    return True

# Main function
def main():
    # Taking input for password list
    print("Enter passwords separated by commas (e.g., abc12345,abc,123456789):")
    password_input = input("Enter passwords: ")
    password_list = [password.strip() for password in password_input.split(",")]

    # Taking input for criteria
    print("\nEnter criteria numbers you want to check (e.g., 1 3 4):")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Special characters (!, @, #)")

    criteria_input = input("Enter your criteria (space-separated numbers): ")
    criteria = list(map(int, criteria_input.split()))

    # Validating each password
    for password in password_list:
        validate_password(password, criteria)

if __name__ == "__main__":
    main()
