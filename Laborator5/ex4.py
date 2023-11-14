class Employee:

    def __init__(self,name,worked_hours,salary):
        self.name=name
        self.worked_hours=worked_hours
        self.salary=salary

    def display(self):
        return f"Name: {self.name}, Number of worked hours: {self.worked_hours}, Salary: {self.salary}"
    
class Manager(Employee):

    def __init__(self, name, worked_hours, salary,team_no):
        super().__init__(name, worked_hours, salary)
        self.team_no=team_no
    
    def display(self):
        return f"Name: {self.name}, Number of worked hours: {self.worked_hours}, Salary: {self.salary}, Number of teams: {self.team_no}"
    
    def teams(self):
        return f"{self.name} is manager over {self.team_no} teams."

class Engineer(Employee):

    def __init__(self, name, worked_hours, salary,en_type):
        super().__init__(name, worked_hours, salary)
        self.en_type=en_type
    
    def display(self):
        return f"Name: {self.name}, Number of worked hours: {self.worked_hours}, Salary: {self.salary}, Engineer type: {self.en_type}"
    
    def about_en(self):
        return f"{self.name} is a {self.en_type} engineer."

class Salesperson(Employee):

    def __init__(self, name, worked_hours, salary,sales):
        super().__init__(name, worked_hours, salary)
        self.sales=sales
    
    def display(self):
        return f"Name: {self.name}, Number of worked hours: {self.worked_hours}, Salary: {self.salary}, Number of sales: {self.sales}"
    
    def how_many_sales(self):
        return f"{self.name} has {self.sales} sales."


employee1 = Employee(name="John", worked_hours=160, salary=50000)
manager1 = Manager(name="Alice", worked_hours=180, salary=70000, team_no=3)
engineer1 = Engineer(name="Bob", worked_hours=160, salary=60000, en_type="Software")
salesperson1 = Salesperson(name="Charlie", worked_hours=160, salary=55000, sales=50)


print(employee1.display())


print(manager1.display())
print(manager1.teams())


print(engineer1.display())
print(engineer1.about_en())


print(salesperson1.display())
print(salesperson1.how_many_sales())
