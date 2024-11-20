def per_func(s, strt, end):
    if strt == end:
        print("".join(s))
    else:
        for i in range(strt, end + 1):
            s[strt], s[i] = s[i], s[strt]
            per_func(s, strt + 1, end)
            s[strt], s[i] = s[i], s[strt]
string = input("Enter a string: ")
s = list(string)
n = len(s)
per_func(s, 0, n - 1)
