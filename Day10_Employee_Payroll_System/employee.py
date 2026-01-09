class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}")