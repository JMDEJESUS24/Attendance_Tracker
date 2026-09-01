# Attendance Tracker App for Python Programming Assesment 2
# Date: 2026-09-01
# Team 4 - Jeremiah de Jesus, Ellen Tran, Nalin Rasupinghe, Saba Firdous
import csv
from datetime import date

# Get student's name (Ellen Tran)
# This is the function to ask for the first and last name and return those values
def get_student():
    first_name = input("Enter student's first name? ")
    last_name = input("Enter student's last name? ")
    
    return first_name, last_name

# Get attendance (Nalin Rasupinghe)
# This is the function to ask if the student is present or absent and return those values
# It also make sure that it handles lower and upper case inputs of 'y'
def get_attendace():
    present = input("Is the student present? (y/n) ")
    
    if present.lower() == 'y':
        return 'Present'
    else:
        return 'Absent'

# Save attendace to CSV (Saba Firdous)
# This is the function to save the attendance to a CSV file. 
# It takes in a list of students and writes it to a CSV file with the appropriate headers.
def save_attendance(students):
    with open('attendance.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'date', 'status'])
        writer.writeheader()
        writer.writerows(students)

# Main attendace tracking function (Jeremiah de Jesus)
# This is the main function that runs the attendance tracking program. 
# It calls the other functions to get the student's name, attendance status, and save the data to a CSV file. It also handles the loop for entering multiple students.
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

# This is the line that starts the program by calling the main function.
record_attendance()
