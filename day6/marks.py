print("This program calculates the average marks of a student.")
total_marks=0
i=0
subjects=int(input("Enter how many subjects are there: "))

marks=[]
while i<subjects:
    print("Subject",i+1)
    marks.append(int(input("Enter the marks of subject ")))#adds another subject's marks to the list
    print("Marks of subject",i+1,"is",marks[i])  
    total_marks=total_marks+marks[i]
    i=i+1

#total_marks and i were outside the loop so they were not being reset to 0 for each subject
# which is why the loop was repeating


print("Total marks:", total_marks)
average_marks=total_marks/subjects
print("Average marks:", average_marks)

if(average_marks>=90):
   print("Grade: A+")  
elif(average_marks>=80):
    print("Grade: A")
elif(average_marks>=70):
   print("Grade: B+")
elif(average_marks>=60):
   print("Grade: B")
elif(average_marks>=50):
   print("Grade: C+")
elif(average_marks>=40):
   print("Grade: C")
elif(average_marks>=35):
   print("Grade: D")
else:
   print("Grade: F")