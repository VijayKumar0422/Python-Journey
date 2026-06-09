emails = set() 

for i in range (5) :
    email = input("Enter email => ")
    emails.add(email)

print ("\nunique Emails => ")
for email in emails:
    print(email)

print("\nTotal unique emails => ", len(emails))