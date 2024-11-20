def is_balanced(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)  # Push opening brackets onto the stack
        elif char in ')}]':
            # Check if the stack is empty or the top of the stack doesn't match
            if not stack or stack.pop() != matching_parentheses[char]:
                return "The input string is NOT balanced."
    
    # If the stack is empty at the end, the string is balanced
    return "The input string is balanced." if not stack else "The input string is NOT balanced."

# Take input from the user
input_string = input("Enter a string with parentheses, brackets, or braces: ")
print(is_balanced(input_string))
