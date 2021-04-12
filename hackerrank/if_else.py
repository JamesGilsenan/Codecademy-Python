n = 22
weird = "Weird"
not_weird = "Not Weird"

if n % 2 == 1:
    print(weird)
elif n % 2 == 0 and n >= 2 and n <= 5:
    print(not_weird)
elif n % 2 == 0 and n in range(6, 21):
    print(weird)
elif n % 2 == 0 and n > 20:
    print(not_weird)