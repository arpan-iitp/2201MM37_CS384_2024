import os

# Function to validate password based on selected criteria
def validate_password_file(password, criteria):
    if len(password) < 8:
        return f'"{password}" is Invalid. Less than 8 Characters.', False

    # Checking criteria
    if 1 in criteria and not any(char.isupper() for char in password):
        return f'"{password}" is Invalid. Missing Uppercase letters.', False
    if 2 in criteria and not any(char.islower() for char in password):
        return f'"{password}" is Invalid. Missing Lowercase letters.', False
    if 3 in criteria and not any(char.isdigit() for char in password):
        return f'"{password}" is Invalid. Missing Numbers.', False
    if 4 in criteria and not any(char in "!@#" for char in password):
        return f'"{password}" is Invalid. Missing Special characters (!, @, #).', False
    if any(char == '$' for char in password):
        return f'"{password}" is Invalid. It contains $ which is not allowed.', False

    return f'"{password}" is Valid.', True

# Main function for reading from file
def validate_passwords_from_file():
    print("Enter criteria numbers you want to check (e.g., 1 3 4):")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Special characters (!, @, #)")

    criteria_input = input("Enter your criteria (space-separated numbers): ")
    criteria = list(map(int, criteria_input.split()))

    valid_count = 0
    invalid_count = 0

    # Determine the file path inside the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'input.txt')

    try:
        # Reading passwords from file
        with open(file_path, 'r') as file:
            for password in file:
                password = password.strip()  # Remove extra spaces/newline
                message, is_valid = validate_password_file(password, criteria)
                print(message)
                if is_valid:
                    valid_count += 1
                else:
                    invalid_count += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print(f"\nTotal Valid Passwords: {valid_count}")
    print(f"Total Invalid Passwords: {invalid_count}")

# Programmatic creation of the input.txt file for testing
# def create_input_file():
#     # Determine the file path inside the script directory
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(script_dir, 'input.txt')

#     passwords = [
#         "abc12345",
#         "abc",
#         "123456789",
#         "abcdefg$",
#         "abcdefgABHD!@313",
#         "abcdefgABHD$$!@313"
#     ]
#     with open(file_path, 'w') as file:
#         file.write("\n".join(passwords))

if __name__ == "__main__":
    # Create the input.txt file (only needed if file doesn't exist)
    # create_input_file()

    # Validate passwords from the file
    validate_passwords_from_file()
