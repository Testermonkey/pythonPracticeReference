from employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee
                

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print('current employees')
        for i in self.employees:
            print(i.fname, i.lname)
 
def main():
    my_company = Company()
    employee1 = SalaryEmployee('Sarah', 'Terry', 60000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Alex', 'Underwood', 60, 40)
    my_company.add_employee(employee2)
    employee3 = ComissionEmployee('Bob', 'Lewous', 400000, 5, 200)
    my_company.add_employee(employee3)
    employee4 = Employee('Lisa', 'Arnold')
    my_company.add_employee(employee4)
    #print(my_company.employees)
    print(my_company.display_employees())

main()
