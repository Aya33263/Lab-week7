# Student Attendance System using OOP in Python
# by Aya Alzwghaibi

import random

# Requirement 3: Store all student records in a list for later use
students = []

class AttendanceSystem:
    def __init__(self, name=None, course_name=None, attendance=0):
        # Initializing basic attributes
        self.name = name
        self.course_name = course_name
        self.attendance = attendance 
        
        # Requirement 2: Automatically generate a unique student ID for each student
        # We start with a random number between 100 and 300
        self.next_id = random.randint(100, 300)

    # Requirement 1: Add attendance records by entering name, attendance, and course
    def add_student(self):
        name = input("Enter Name: ")
        course_name = input("Enter Course name: ")
        attendance = float(input("Enter Attendance %: "))
        
        # We store the data in a dictionary to keep it organized
        student_data = {
            "id": self.next_id,
            "name": name,
            "course": course_name,
            "attendance": attendance
        }
        
        # Add the dictionary to our list
        students.append(student_data)
        print(f"NEW STUDENT ID is: {self.next_id}")
        
        # Ensure the next ID is unique by incrementing it
        self.next_id += 1 

    # Requirement 5: Display all stored student records clearly for review
    def display_all(self):
        print("\n--- Student List ---")
        if not students:
            print("No records found.")
            return
            
        for s in students:
            print(f" Name: {s['name']} |ID: {s['id']} | Course: {s['course']} | Attendance: {s['attendance']}%")

    # Requirement 4: Update a record by searching with ID and modifying details
    def update_student(self):
        search_id = int(input("Enter Student ID to update: "))
        for s in students:
            if s["id"] == search_id:
                # Modifying both attendance and course details as per requirements
                s["course"] = input("Enter new course name: ")
                s["attendance"] = float(input("Enter new attendance percentage: "))
                print(f"Update Successful for student ID {s['id']}")
                return
        print("ID not found.")

    # Requirement 6: Calculate the average attendance percentage for all students
    def show_average(self):
        if not students:
            print("No data available to calculate average.")
            return
        
        # Sum up all attendance values and divide by the total number of students
        total = sum(s["attendance"] for s in students)
        average = total / len(students)
        print(f"\n--- System Statistics ---")
        print(f"Average Attendance: {average}%")


# --- The Main Program Loop ---

# Save the class in one variable (Object creation)
system = AttendanceSystem()

while True:
    print(" \nSTUDENT SYSTEM MENU: ")
    print("1. Add New Student")
    print("2. Display All Records")
    print("3. Update Attendance/Course")
    print("4. Calculate Average")
    print("5. Exit Program")
    
    choice = input("\nSelect an option (1-5): ")

    # Navigation logic based on user selection
    if choice == '1':
        system.add_student()
    elif choice == '2':
        system.display_all()
    elif choice == '3':
        system.update_student()
    elif choice == '4':
        system.show_average()
    elif choice == '5':
        print("Closing the system. Goodbye!")
        break 
    else:
        print("Invalid selection! Please choose from 1 to 5.")
