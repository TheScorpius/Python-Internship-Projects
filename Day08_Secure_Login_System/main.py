from auth import register_user, login_user

def main():
    while True:
        print("\nSecure Login System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                register_user(username, password)
                print("Registration successful")

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password ")
                if login_user(username, password):
                    print("Login successful")
                else:
                    print("Invalid credentials")

            elif choice == "3":
                print("Exiting system...")
                break

            else:
                print("Invalid option")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()