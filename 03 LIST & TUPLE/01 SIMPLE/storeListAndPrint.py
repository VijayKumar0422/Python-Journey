numbers = []

for i in range (5):
    num = int (input("Enter Number : "))
    numbers.append(num)

print("Largest =", max(numbers))
print("Smallest =", min(numbers))
print("Sum =", sum(numbers))
