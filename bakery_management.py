import sqlite3
import time


DB_FILE = "bakery.db"
ADMIN_PASSWORD = "admin123"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Menu (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            product_price REAL NOT NULL
        )
        """
    )
    conn.commit()
    return conn, cursor


def seed_menu_if_empty(cursor, conn):
    cursor.execute("SELECT COUNT(*) FROM Menu")
    count = cursor.fetchone()[0]
    if count == 0:
        sample_items = [
            ("Cake", 400),
            ("Bread", 50),
            ("Cookies", 100),
            ("Doughnuts", 80),
            ("Pie", 120),
        ]
        cursor.executemany(
            "INSERT INTO Menu (product_name, product_price) VALUES (?, ?)",
            sample_items,
        )
        conn.commit()


def show_menu(cursor):
    print("\n--- Bakery Menu ---")
    cursor.execute("SELECT product_id, product_name, product_price FROM Menu")
    for product_id, name, price in cursor.fetchall():
        print(f"{product_id}. {name} - Rs. {price:.2f}")
    print()


def admin_menu(cursor, conn):
    while True:
        print("\nAdmin Menu")
        print("1. Add Item")
        print("2. Update Item Price")
        print("3. Delete Item")
        print("4. Show Menu")
        print("5. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter price: ").strip())
                cursor.execute(
                    "INSERT INTO Menu (product_name, product_price) VALUES (?, ?)",
                    (name, price),
                )
                conn.commit()
                print(f"Added {name} priced at Rs. {price:.2f}")
            except ValueError:
                print("Invalid price.")

        elif choice == "2":
            show_menu(cursor)
            try:
                product_id = int(input("Enter product id to update: ").strip())
                new_price = float(input("Enter new price: ").strip())
                cursor.execute(
                    "UPDATE Menu SET product_price = ? WHERE product_id = ?",
                    (new_price, product_id),
                )
                conn.commit()
                print("Price updated.")
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            show_menu(cursor)
            try:
                product_id = int(input("Enter product id to delete: ").strip())
                cursor.execute("DELETE FROM Menu WHERE product_id = ?", (product_id,))
                conn.commit()
                print("Item deleted.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            show_menu(cursor)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")

        time.sleep(0.5)


def customer_billing(cursor):
    cart = []
    total = 0.0

    while True:
        show_menu(cursor)
        selection = input("Enter product id to buy, or 'done' to finish: ").strip()
        if selection.lower() == "done":
            break

        try:
            product_id = int(selection)
            quantity = int(input("Quantity: ").strip())
            cursor.execute(
                "SELECT product_name, product_price FROM Menu WHERE product_id = ?",
                (product_id,),
            )
            row = cursor.fetchone()

            if row is None:
                print("Invalid product id.")
                continue

            name, price = row
            cost = price * quantity
            cart.append((name, quantity, price, cost))
            total += cost
            print(f"Added {quantity} x {name} = Rs. {cost:.2f}")
        except ValueError:
            print("Invalid input.")

    print("\n--- Bill ---")
    for name, quantity, price, cost in cart:
        print(f"{name} x {quantity} @ Rs. {price:.2f} each = Rs. {cost:.2f}")
    print(f"Total amount: Rs. {total:.2f}")


def main():
    conn, cursor = init_db()
    seed_menu_if_empty(cursor, conn)

    while True:
        print("\n========================")
        print("Welcome to The Bakery")
        print("1. Admin Login")
        print("2. Customer Purchase")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            password = input("Enter admin password: ").strip()
            if password == ADMIN_PASSWORD:
                admin_menu(cursor, conn)
            else:
                print("Wrong password.")
                time.sleep(0.5)

        elif choice == "2":
            customer_billing(cursor)
            input("Press Enter to continue...")

        elif choice == "3":
            print("Thank you. Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

    conn.close()


if __name__ == "__main__":
    main()
