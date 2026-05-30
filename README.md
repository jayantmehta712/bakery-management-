# Bakery Management System

A terminal-based bakery management application built in Python with SQLite. It supports two modes of operation — an admin panel for managing the menu and a customer billing interface for placing orders and generating bills.

---

## Overview

This application simulates a point-of-sale system for a small bakery. On first run, the database is initialised and seeded with sample menu items. An admin can log in to manage products, while customers can browse the menu, add items to a cart, and receive a printed bill.

---

## Repository Structure

```
bakery-management-/
└── # bakery_management by jayant in py.py    # Main Python script
```

---

## Features

**Admin Panel**
- Add new items to the menu
- Update the price of existing items
- Delete items from the menu
- View the current menu

**Customer Billing**
- Browse the live menu
- Select items and specify quantities
- Automatically calculates and prints an itemised bill with the total amount

**Database**
- Uses SQLite for persistent menu storage
- Automatically creates and seeds the database on first run with sample items (Cake, Bread, Cookies, Doughnuts, Pie)

---

## Requirements

- Python 3.7+
- No third-party packages required — uses only the Python standard library (`sqlite3`, `time`)

---

## Getting Started

### Run the application

```bash
python "# bakery_management by jayant in py.py"
```

On first launch, the database file `bakery.db` is created automatically and pre-populated with sample menu items.

---

## Usage

### Main Menu

```
========================
Welcome to THE BAKERY
1) Admin Login
2) Customer Purchase
3) Exit
```

### Admin Login

The default admin password is `admin123`. This can be changed directly in the source code.

Once logged in, the admin can add, update, or delete items from the menu.

### Customer Purchase

The customer selects items by product ID and specifies a quantity. After entering all desired items, typing `done` prints the itemised bill:

```
--- BILL ---
Cake x 1 @ ₹400.00 each = ₹400.00
Bread x 2 @ ₹50.00 each = ₹100.00
Total amount: ₹500.00
```

---

## Database

| Table   | Columns                                              |
|---------|------------------------------------------------------|
| `Menu`  | `product_id` (PK), `product_name`, `product_price`  |

The database file `bakery.db` is created in the same directory as the script.

---

## Default Menu Items

| Product    | Price (INR) |
|------------|-------------|
| Cake       | ₹400        |
| Bread      | ₹50         |
| Cookies    | ₹100        |
| Doughnuts  | ₹80         |
| Pie        | ₹120        |

These are seeded automatically on first run only if the menu table is empty.

---

## Author

**Jayant Mehta**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jayant-mehta-b2752a302/)

---
