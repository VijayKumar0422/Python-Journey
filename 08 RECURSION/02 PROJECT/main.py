def countdown(n):
    if n == 0:
        return 0

    print(n)
    return 1 + countdown(n - 1)

num = int(input("Enter Number => "))

total = countdown(num)

print("Total Numbers Printed =", total)