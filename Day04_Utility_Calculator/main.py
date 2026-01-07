from utilities.basic import add, subtract, multiply, divide
from utilities.finance import simple_interest, emi
from utilities.conversion import celsius_to_fahrenheit, km_to_miles
from utilities.health import calculate_bmi, bmi_category

def utility_calculator():
    while True:
        print("\n--- Utility Calculator ---")
        print("1. Basic Calculator")
        print("2. Finance Utilities")
        print("3. Unit Conversions")
        print("4. BMI Calculator")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Add:", add(a, b))
            print("Subtract:", subtract(a, b))
            print("Multiply:", multiply(a, b))
            print("Divide:", divide(a, b))

        elif choice == "2":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            print("Simple Interest:", simple_interest(p, r, t))
            print("Monthly EMI:", round(emi(p, r, t), 2))

        elif choice == "3":
            c = float(input("Temperature (Celsius): "))
            km = float(input("Distance (KM): "))
            print("Fahrenheit:", celsius_to_fahrenheit(c))
            print("Miles:", km_to_miles(km))

        elif choice == "4":
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            print(f"Your BMI is: {bmi}")
            print(f"Category: {category}")

        elif choice == "5":
            print("Utility Calculator closed.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    utility_calculator()