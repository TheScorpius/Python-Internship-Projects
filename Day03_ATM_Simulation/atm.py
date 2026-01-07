def atm_system():
    balance = 10000
    correct_pin = "1234"
    attempts = 3

    print("Welcome to Python ATM")

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("\nLogin successful!")

            while True:
                print("\n--- ATM Menu ---")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")

                choice = input("Choose an option (1-4): ")

                if choice == "1":
                    print(f"Current Balance: ₹{balance}")

                elif choice == "2":
                    amount = int(input("Enter deposit amount: ₹"))
                    if amount > 0:
                        balance += amount
                        print(f"₹{amount} deposited successfully.")
                    else:
                        print("Invalid amount.")

                elif choice == "3":
                    amount = int(input("Enter withdrawal amount: ₹"))
                    if amount <= 0:
                        print("Invalid amount.")
                    elif amount > balance:
                        print("Insufficient balance.")
                    else:
                        balance -= amount
                        print(f"₹{amount} withdrawn successfully.")

                elif choice == "4":
                    print("Thank you for using Python ATM.")
                    return

                else:
                    print("Invalid option. Try again.")

        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")

    print("Account locked due to multiple failed attempts.")


if __name__ == "__main__":
    atm_system()