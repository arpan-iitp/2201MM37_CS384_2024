def string_compression(s):
    com_str = ""
    length = len(s)
    i = 0
    while i < length:
        count = 1
        while i + 1 < length and s[i] == s[i + 1]:
            count += 1
            i += 1
        com_str += s[i] + str(count)
        i += 1
    return com_str

string = input("Enter a string:")

com_res = string_compression(string)
print(f"the compressed version of '{string}' is: '{com_res}'")