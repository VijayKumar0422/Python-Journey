user = {}

user["name"] = input("Enter name => ")
user["age"] = int(input("Enter age => "))
user["city"] = input("Enter city => ")

print ("\nuser profile ")

for key, value in user .items():
    print (key, ":", value)