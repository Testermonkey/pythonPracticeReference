class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def run_tests(self):
        print(f'Testing is started by {self.name}')
        print('Tests are complete')

class Developer(Employee):
    __slots__ = ("name", "age", "salary", "framework") ## this could and should be in Employee

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus

    def has_slots(self):
        return hasattr(self, "__slots__")

emp1 = Tester('Lauren', 44, 1000)
emp2 = Developer('Ji-Soo', 38, 100, "Django")


# emp1.increase_salary(20)
# emp2.increase_salary(20, 30)
# print(emp1.salary)
# print(emp2.salary)

print(emp2.name, emp2.framework)
print(emp2.__slots__)
print(emp2.has_slots())