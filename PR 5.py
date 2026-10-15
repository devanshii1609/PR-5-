from abc import ABC, abstractmethod

# ==========================
# Base Employee Class
# ==========================
class Employee:
    company = "Tech Solutions Ltd"

    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.__name = name
        self.__age = age
        self.__salary = salary

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 18:
            self.__age = age
        else:
            print("Age must be above 18.")

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")

    def display_info(self):
        print("\n-----------------------------")
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.__name}")
        print(f"Age         : {self.__age}")
        print(f"Salary      : ₹{self.__salary}")

    # Method Overloading Simulation
    def calculate_bonus(self, bonus=0):
        return self.__salary + bonus

    # Operator Overloading
    def __str__(self):
        return f"{self.emp_id} - {self.__name}"


# ==========================
# Abstract Class
# ==========================
class Role(ABC):

    @abstractmethod
    def work(self):
        pass


# ==========================
# Manager Class
