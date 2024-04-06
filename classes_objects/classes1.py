class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return (f"{self.name} is {self.age} years old\nEmployee is {self.position} with the salary of ${self.salary}")
    
    def __repr__(self):
        return(
            f"{repr(self.name)}, {repr(self.age)},"
            f"{repr(self.position)}, {repr(self.salary)}"
        )
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError("Minimum was is $1000")
        self._annual_salary = None
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary

    # def get_salary(self):
    #     # return f"${self.salary}" ## for returning currency values
    #     # return round(self.salary, 2)  ## for returning decimal values
    #     # return logging.info("someone has access the salary attribute")
    #     return self.salary
    
    # def set_salary(self, salary):
    #     if salary < 1000:
    #         raise ValueError("Minimum was is $1000")
    #     self._salary = salary ## underscore indicates non-public attribute
        #self.__salary = salary ## duble underscore is name mangeling - not used much
    
    

e1 = Employee("Bob Terry", 56, "developer", 1200)
e2 = Employee("Bob bob", 56, "developer", 1200)
# print(e1.__dict__)
# print(e2.__dict__)
#
# e1.info()
# print(e1)
# print(repr(e1))
# e1.salary=2100
# print(e1.salary)
print(e1.annual_salary)
e1.salary = 1000
print(e1.annual_salary)