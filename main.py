import csv
import os

DATA_FILE = "data/expenses.csv"


def load_expenses():
    items = []

    if os.path.isfile(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) != 3:
                    continue

                date, amount, category = row

                try:
                    amount = float(amount)
                except ValueError:
                    continue

                items.append({
                    "date": date,
                    "amount": amount,
                    "category": category
                })

    return items


def save_expenses(data):
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        for entry in data:
            writer.writerow([entry["date"], entry["amount"], entry["category"]])


def add_expense(data):
    date = input("Date (YYYY-MM-DD): ").strip()

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("That doesn’t look like a number.")
        return

    category = input("Category: ").strip()

    data.append({
        "date": date,
        "amount": amount,
        "category": category
    })

    print("Added.")


def view_expenses(data):
    if not data:
        print("Nothing recorded yet.")
        return

    print("\nDate        | Amount   | Category")
    print("-" * 34)

    for entry in data:
        print(f"{entry['date']} | {entry['amount']:.2f} | {entry['category']}")


def total_spent(data):
    total = sum(item["amount"] for item in data)
    print(f"Total spent so far: {total:.2f}")


def summary_by_category(data):
    summary = {}

    for item in data:
        cat = item["category"]
        summary[cat] = summary.get(cat, 0) + item["amount"]

    if not summary:
        print("No category data found.")
        return

    print("\nCategory    | Total")
    print("-" * 26)

    for cat, amount in summary.items():
        print(f"{cat:10} | {amount:.2f}")


def main():
    if not os.path.exists("data"):
        os.makedirs("data")

    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add an expense")
        print("2. Show all expenses")
        print("3. Show total spent")
        print("4. Category summary")
        print("5. Save")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_spent(expenses)
        elif choice == "4":
            summary_by_category(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Saved.")
        elif choice == "6":
            save_expenses(expenses)
            print("Exiting...")
            break
        else:
            print("Try again.")


if __name__ == "__main__":
    main()