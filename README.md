# 📊 Student Attendance Prototype

A specialized Python management system built using **Object-Oriented Programming (OOP)**. This prototype allows training institutes to automate the tracking of student attendance, course enrollment, and performance analytics.

## 🎯 Project Requirements
This application was developed to satisfy the following institutional needs:
1. **Dynamic Enrollment**: Capture names, courses, and attendance percentages.
2. **Automated ID System**: Secure, unique ID generation for every new entry.
3. **Record Management**: A centralized database (list) for all student profiles.
4. **Data Modification**: Update existing records via targeted ID search.
5. **System Transparency**: Clear display of all stored data.
6. **Performance Analytics**: Real-time calculation of global attendance averages.

---

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine:

### 1. Prerequisites
Ensure you have **Python 3.x** installed. You can check your version by running:
```bash
python --version

# 2. Clone the Repository
Download the project files to your computer
# 3. Run the Application
Start the interactive menu-driven system
--------------------------------------------------
🏗️ Technical Architecture
The system is designed with a modular approach to separate data entry from data processing.

 Core Components
1 # The List (students): Acts as a volatile database storing student dictionaries.

2 # The Class (AttendanceSystem): The engine that handles all logic.

3 # add_student(): Uses Dictionaries to map keys (ID, Name, Course) to user input.

4 # update_student(): Implements a Linear Search algorithm to find and modify records.

5 # show_average(): Uses Aggregators to calculate mean percentages

 💻Usage Guide
1-Add Student // Enter details; system assigns a unique ID from 100-300.
2-Display Records // Prints a formatted roster of all registered students.
3-Update Record // Enter the Student ID to modify course or attendance data.
4-Calculate Average // View the overall performance of the entire institute.
5-Exit // Safely close the application.

# 📝 Programming Concepts Demonstrated
Encapsulation: Keeping all attendance logic within a dedicated class.

Data Mapping: Using key-value pairs for efficient data retrieval.

Randomization: Using the random library for unique ID seeding.

Input Validation: Ensuring float and integer types for mathematical calculations.

# 🛠️ Tools Used
Language: Python 3.x

Version Control: GitHub

Environment: VS Code
