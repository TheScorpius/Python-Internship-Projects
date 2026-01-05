def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"

def main():
    name = input("Enter student name: ")

    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))

    total = m1 + m2 + m3
    average = total / 3
    grade = calculate_grade(average)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

if __name__ == "__main__":
    main()