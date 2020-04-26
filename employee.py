class Employee(object):
    def __init__(self,employee_name):
        self.employee_name = employee_name
    def earnings(self,hours): # both classes have the same earnings function but its "overided" for the 2nd class. 
        self.hours = hours
        print(hours * 20.00)
class parttimeEmployee(Employee): # the parameter of this class is a class
    def earnings(self,hours):
        self.hours = hours
        print(hours * 12.00)

first = Employee("Fabian")
second = parttimeEmployee("Bryan")
first.earnings(8)
second.earnings(8)