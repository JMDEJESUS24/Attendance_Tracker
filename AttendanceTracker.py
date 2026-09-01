# ==== FUNCTION ====
import csv
from datetime import date

# Get student's name (Ellen Tran)
def get_student():
    first_name = input("Enter student's first name? ")
    last_name = input("Enter student's last name? ")
    
    return first_name, last_name

# Get attendance (Nalin Rasupinghe)
def get_attendace():
    present = input("Is the student present? (y/n) ")
    
    if present.lower() == 'y':
        return 'Present'
    else:
        return 'Absent'

# Save attendace to CSV (Saba Firdous)
def save_attendance(students):
    with open('attendance.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'date', 'status'])
        writer.writeheader()
        writer.writerows(students)

# Main attendace tracking function (Jeremiah de Jesus)
def record_attendance():
    students = []
    
    while True:
        first_name, last_name = get_student()
        status = get_attendace()
        
        students.append({
            'first_name': first_name,
            'last_name': last_name,
            'date': date.today().strftime("%Y-%m-%d"),
            'status': status
        })
        
        save_attendance(students)
        
        print("Attendance recorded successfully.")
        
        another = input("Do you want to enter another student? (y/n) ")
        
        if another.lower() != 'y':
            break
    
    print("Attendance tracking completed. Goodbye!")

# Start the program
record_attendance()
