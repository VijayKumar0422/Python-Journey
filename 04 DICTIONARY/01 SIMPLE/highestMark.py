marks = {
    "math" : 80,
    "science" : 95,
    "english" : 88
}

highest_subject = max (marks, key = marks.get)

print ("Highest marks subject => ", highest_subject)
print ("Marks => ", marks[highest_subject])