students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks (%): "))
    s1 = float(input("Enter Subject 1 marks: "))
    s2 = float(input("Enter Subject 2 marks: "))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter family income: "))

    if (marks >= 75 and s1 >= 50 and s2 >= 50
            and attendance >= 75 and income <= 200000):
        students.append([name, marks])
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")

# Rank students by aggregate marks
students.sort(key=lambda x: x[1], reverse=True)

print("\n--- Scholarship Merit List ---")

for rank, student in enumerate(students, start=1):
    print(rank, student[0], student[1], "%")