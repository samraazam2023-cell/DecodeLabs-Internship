expenses = []


def add_expense():
    print("\n---------- ADD EXPENSE ----------")

    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expenses.append({
            "name": name,
            "amount": amount
        })

        print(f"✓ Expense '{name}' added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a number.")


def view_expenses():
    print("\n========== YOUR EXPENSES ==========")

    if not expenses:
        print("No expenses have been added yet.")
        return

    total = 0

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['name']:<20} "
            f"Rs. {expense['amount']:.2f}"
        )
        total += expense["amount"]

    print("-----------------------------------")
    print(f"Total Spent:             Rs. {total:.2f}")


def view_total():
    total = sum(expense["amount"] for expense in expenses)

    print("\n========== TOTAL SPENT ==========")
    print(f"Total Spent: Rs. {total:.2f}")


def main():
    print("======================================")
    print("          💰 EXPENSE TRACKER")
    print("======================================")

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total()

        elif choice == "4":
            print("\nThank you for using Expense Tracker!")
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
