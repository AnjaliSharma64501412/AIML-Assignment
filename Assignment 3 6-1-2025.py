marks1 = float(input("Enter marks for Maths: "))
marks2 = float(input("Enter marks for Science: "))
marks3 = float(input("Enter marks for Social: "))

average = (marks1 + marks2 + marks3) /3
print(average)
if average >= 90:
    print("Grade: A")
elif 80 <= average < 90:
    print("Grade: B")
elif 70 <= average < 80:
    print("Grade: C")
else:
    print("Grade: Fail")
