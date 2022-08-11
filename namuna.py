n = int(input("Write integer number: "))
print(n)
if n % 2:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weirf")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and 20 < n:
    print("Not Weird")
elif 1 >= n >= 100:
    print("Write number in range 1-100")
