def moderate_results(student_records, grace_marks=5, max_limit=100):
    """
    Moderates student examination marks.

    Parameters:
    - student_records: List of dictionaries containing student names and subject marks.
    - grace_marks: Points to add during moderation.
    - max_limit: Maximum possible score for any subject.
    """
    moderated_records = []

    for student in student_records:
        name = student["name"]
        original_marks = student["marks"]
        moderated_marks = {}

        for subject, score in original_marks.items():
            # Apply moderation rule: add grace marks
            new_score = score + grace_marks

            # Preserve maximum-mark constraints (cannot exceed max_limit)
            new_score = min(new_score, max_limit)

            moderated_marks[subject] = new_score

        moderated_records.append({
            "name": name,
            "original": original_marks,
            "moderated": moderated_marks
        })

    return moderated_records


# --- Example Usage ---
if __name__ == "__main__":
    # Sample data: Students with marks in Math, Physics, and Chemistry
    students = [
        {"name": "Alice Smith", "marks": {"Math": 45, "Physics": 52, "Chemistry": 60}},
        {"name": "Bob Jones", "marks": {"Math": 97, "Physics": 98, "Chemistry": 92}},  # Close to max cap
        {"name": "Charlie Brown", "marks": {"Math": 32, "Physics": 40, "Chemistry": 38}}
    ]

    # Run moderation (+5 grace marks, cap at 100)
    results = moderate_results(students, grace_marks=5, max_limit=100)

    # Display comparison report
    print("=" * 50)
    print("UNIVERSITY EXAMINATION RESULT MODERATION REPORT")
    print("=" * 50)

    for record in results:
        print(f"\nStudent: {record['name']}")
        print(f"{'Subject':<12} | {'Original':<10} | {'Moderated':<10}")
        print("-" * 38)

        for subject in record["original"]:
            orig = record["original"][subject]
            mod = record["moderated"][subject]
            print(f"{subject:<12} | {orig:<10} | {mod:<10}")