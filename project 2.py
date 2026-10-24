
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
target = float(input("Enter required attendance (%): "))

current = (attended / total) * 100
print("Current attendance:", round(current, 2), "%")

if current >= target:
    print("You are already eligible.")
else:
    required = 0
    while (attended + required) / (total + required) * 100 < target:
        required += 1

    print("Minimum consecutive classes to attend:", required)
    print("Attendance after recovery:",
          round((attended + required) / (total + required) * 100, 2), "%")
