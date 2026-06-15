text = input("Enter text => ")

with open ("data.txt", "w") as file :
    file.write (text)

print ("Data saved successfully")