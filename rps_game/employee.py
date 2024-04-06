class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
        
    def calc_pay(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    
    def calc_pay(self):
        return self.weekly_hours * self.weekly_hours

class ComissionEmployee(Employee):
    def __init__(self, fname, lname, salary, total_sales, comission_rate):
        super().__init__(fname, lname)
        self.salary = salary
        self.total_sales = total_sales
        self.comission_rate = comission_rate
    
    def calc_pay(self):
        return (self.total_sales * self.comission_rate) + (self.salary/52)