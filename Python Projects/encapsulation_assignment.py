class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary value!")

    def _display_employee_info(self):
        print(f"Employee: {self.name}, Age: {self._age}, Salary: {self.__salary}")

emp = Employee("John Doe", 30, 50000)

print("Employee Name:", emp.name)
print("Employee Age:", emp._age)
print("Employee Salary:", emp.get_salary())

emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())

emp._display_employee_info()
