class PayrollSystem:
    def process_payroll(self, employees):
        print("\nProcessing Payroll\n")
        for emp in employees:
            emp.display()
            print("Salary:", emp.calculate_salary())
            print("-" * 30)