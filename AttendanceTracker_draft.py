# ==== FUNCTION ====
import csv
from datetime import date

students = []

while True:
    first_name = input("Enter student's first name? ")
    last_name = input("Enter student's last name? ")

    present = input("Is the student present? (y/n) ")

    if present.lower() == 'y':
        students.append({
            'first_name': first_name,
            'last_name': last_name,
            'date': date.today().strftime("%Y-%m-%d"),
            'status': 'Present'
        })
    else:
        students.append({
            'first_name': first_name,
            'last_name': last_name,
            'date': date.today().strftime("%Y-%m-%d"),
            'status': 'Absent'
        })

    with open('attendance.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'date', 'status'])
        writer.writeheader()
        writer.writerows(students)

    print("Attendance recorded successfully.")

    another = input("Do you want to enter another student? (y/n) ")

    if another.lower() != 'y':
        break

print("Attendance tracking completed. Goodbye!")





            