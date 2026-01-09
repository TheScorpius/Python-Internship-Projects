FILE_NAME="attendance.txt"

def mark_attendance():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    status = input("Enter status (Present/Absent): ").capitalize()

    if status not in ["Present", "Absent"]:
        print("Invalid status. Please enter 'Present' or 'Absent'.")
        return
    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{status}\n")
    print("Attendance marked successfully.")

def view_attendance():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No attendance records found.")
                return
            print("Roll Number | Name       | Status")
            print("-----------------------------------")
            for record in records:
                roll, name, status = record.strip().split(",")
                print(f"{roll} | {name} | {status}")
    except FileNotFoundError:
        print("No attendance records found.")

def attendance_system():
    while True:
        print("\nAttendance Management System")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    attendance_system()