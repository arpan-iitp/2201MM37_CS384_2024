def u_sum(n):
    while n >= 10:
        sd= 0
        while n > 0:
            sd += n % 10
            n = n // 10
        n = sd
    return n;


number = int(input("Enter an integer: "))

result = u_sum(number)
print(f"the unitry sum of the inputed number is: {result}")