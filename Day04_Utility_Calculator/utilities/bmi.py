def calculate_bmi(weight, height):
    """
    weight: in kilograms
    height: in meters
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("\n--- BMI Calculator ---")

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()