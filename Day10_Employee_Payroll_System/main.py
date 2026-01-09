from fulltime import FullTimeEmployee
from parttime import PartTimeEmployee
from payroll import PayrollSystem

def main():
    employees = [
        FullTimeEmployee(101, "Om", 50000),
        PartTimeEmployee(102, "Amit", 40, 500),
        FullTimeEmployee(103, "Sneha", 60000),
        PartTimeEmployee(104, "Riya", 30, 400)
    ]

    payroll = PayrollSystem()
    payroll.process_payroll(employees)

if __name__ == "__main__":
    main()