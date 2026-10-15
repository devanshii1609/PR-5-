# 🚀 PR 5 - Employee Management System

## 📌 Project Overview
The Employee Management System is a Python-based Object-Oriented Programming (OOP) project that demonstrates key OOP concepts through employee management operations.

### ✅ Concepts Implemented
- Classes & Objects
- Inheritance
- Encapsulation
- Abstraction (ABC Module)
- Method Overriding
- Method Overloading (simulated using default arguments)
- Operator Overloading (`__str__`)
- Polymorphism

## 🏢 Employee Types
### 👨‍💼 Manager
- Manages employees and projects
- Includes department information

### 👨‍💻 Developer
- Develops software applications
- Includes programming language information

### 🎓 Intern
- Learns and assists senior staff
- Includes internship duration

## ⚙️ Features
- Add Employee
- Remove Employee
- Update Employee Salary
- Display Employee Details
- Calculate Bonus
- Encapsulation using Getters and Setters
- Role-based Work Methods

## 📂 Project Structure
```text
Employee (Base Class)
│
├── Manager
├── Developer
└── Intern

Role (Abstract Class)
│
├── work()
```

## 💡 Sample Usage
```python
manager = Manager(101, "Rahul", 35, 75000, "HR")
developer = Developer(102, "Aman", 28, 65000, "Python")
intern = Intern(103, "Priya", 21, 15000, 6)

ems = EmployeeManagementSystem()

ems.add_employee(manager)
ems.add_employee(developer)
ems.add_employee(intern)
```

## 🖥️ Expected Output
```text
Employee Added Successfully!
Employee Added Successfully!
Employee Added Successfully!
```

## 🔒 Encapsulation Example
```python
developer.set_salary(70000)
print(developer.get_salary())
```

## 🎯 Learning Outcomes
This project helps understand:
- OOP Design
- Code Reusability
- Data Hiding
- Abstract Classes
- Employee Record Management

## 🛠️ Suggested Improvements
- File Handling
- Database Integration
- GUI using Tkinter
- Search and Sort Operations
- Report Generation

## 👨‍💻 Author
Devanshi Sharma

---
⭐ Academic Python OOP Project - PR 5
