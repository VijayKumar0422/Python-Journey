set1 = set(map(int, input("Enter first set elements => ").split()))
set2 = set(map(int, input("Enter second set elements => ").split()))

print ("union => ", set1 | set2)
print ("intersection => ", set1 & set2)
print ("difference => ", set1 - set2)