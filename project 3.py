
# Student Timetable Conflict Detection

# (Course, Day, Start Time, End Time, Room)
timetable = [
    ("Python", "Monday", 9, 11, "R101"),
    ("Maths", "Monday", 10, 12, "R102"),
    ("Physics", "Tuesday", 9, 11, "R101")
]

unavailable_rooms = ["R103"]

valid = True

for i in range(len(timetable)):
    course1, day1, start1, end1, room1 = timetable[i]

    if room1 in unavailable_rooms:
        print(course1, "uses unavailable room", room1)
        valid = False

    for j in range(i + 1, len(timetable)):
        course2, day2, start2, end2, room2 = timetable[j]

        if day1 == day2 and start1 < end2 and start2 < end1:
            print("Time conflict:", course1, "and", course2)
            valid = False

            if room1 == room2:
                print("Room conflict:", room1)

if valid:
    print("Timetable is valid")
else:
    print("Timetable has conflicts")
