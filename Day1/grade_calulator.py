grade = int(input("Enter the grade of the student:"))

if(grade>=90 and grade<=100):
    print(f"{grade} A")
elif(grade>=80 and grade<90):
    print(f"{grade} B")
elif(grade>=70 and grade<80):
    print(f"{grade} C")
elif(grade>=60 and grade<70):
    print(f"{grade} D")
if(grade>100):
    print("Invalid")
else:
    print(f"{grade} F")
