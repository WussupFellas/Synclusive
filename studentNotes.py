
num_students = int(input("How many studentes are there: "))

final_notes = []

for _ in range(num_students):
    note = float(input("Enter a note: "))
    final_notes.append(note)

passed_count = 0
failed_count = 0

for note in final_notes:
    if note >= 9.5:
        print(note)
        passed_count += 1
    else:
        failed_count += 1

print(f"Number of students who passed: {passed_count}")
print(f"Number of students who failed: {failed_count}")



