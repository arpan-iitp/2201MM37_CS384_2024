def check_prime(n):
    n = int(n)
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i=5
    while i <= n/2 :
      if n % i == 0:
       return False
      i += 1
    return True

def checkRprime(n):
    s = str(n)
    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        if not check_prime(rotation):
            return False
    return True

numb =input(" enter the number to check for rotational prime ")

if checkRprime(numb):
  print(f"{numb} is a Rotational prime.")
else:
   print(f"{numb} is not a Rotational prime.")