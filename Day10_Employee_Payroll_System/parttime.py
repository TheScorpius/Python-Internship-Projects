from employee import Employee

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, rate_per_hour):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour