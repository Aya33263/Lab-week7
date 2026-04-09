# Student Attendance using OOP IN PYTHON

import random
students = []

class AttendanceSystem:
    def __init__(self, name=None, course_name=None, attendance=0 ):
        self.name = name
        self.course_name = course_name
        self.attendance = attendance 

        self.next_id = random.randint(1,100)

    def add_student(self):
        name = input("Enter Name: ")
        course_name = input("Enter Course name: ")
        attendance = float(input("Enter Attendance %: "))
        
        student_data = {
            "id": self.next_id,
            "name": name,
            "course": course_name,
            "attendance": attendance
        }
        students.append(student_data)
        print(f"Added! ID is {self.next_id}")
        self.next_id += 1 

    def display_all(self):
        print("\n--- Student List ---")
        for s in students:
            print(f"ID: {s['id']} | Name: {s['name']} | Att: {s['attendance']}%")

    def update_student(self):
        search_id = int(input("Enter Student ID to update: "))
        for s in students:
            if s["id"] == search_id:
                s["attendance"] = float(input("Enter new attendance: "))
                print("Update Successful!")
                return
        print("ID not found.")

    def show_average(self):
        if not students:
            return
        total = sum(s["attendance"] for s in students)
        print(f"Average Attendance: {total / len(students)}%")


#save the class in one avarible
# --- the input part---
system = AttendanceSystem()

while True:
    print(" \nSTUDENT SYSTEM MENU\n ")
    print("1. Add New Student")
    print("2. Display All Records")
    print("3. Update Attendance")
    print("4. Calculate Average")
    print("5. Exit Program")
    
    choice = input("\nSelect an option (1-5): ")

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
        print(" Invalid selection! Please choose from 1 to 5.")