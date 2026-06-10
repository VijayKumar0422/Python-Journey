total = 0

for i in range (1, 6) :
    marks = float (input(f"Enter marks subjects {i} "))
    total += marks

average = total / 5

print ("Total marks = ", total)
print("Average marks = ", average)
