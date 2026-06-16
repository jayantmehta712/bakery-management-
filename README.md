# Bakery Management System

A terminal-based bakery management application built with Python and SQLite. It includes an admin menu for managing bakery items and a customer billing flow for creating orders.

## Features

- SQLite database for persistent menu storage.
- Admin login for adding, updating, deleting, and viewing menu items.
- Customer purchase flow with quantity selection.
- Automatic bill generation with item totals and final amount.
- Seeded sample menu on first run.

## Repository Structure

```text
bakery-management-/
  bakery_management.py
  README.md
```

## Requirements

- Python 3.8+

No external packages are required.

## Run

```bash
python bakery_management.py
```

Default admin password:

```text
admin123
```

## Data

The app creates a local SQLite database named `bakery.db` when it runs.

## Interview Talking Points

- Built a menu-driven Python application with persistent SQLite storage.
- Implemented admin and customer workflows.
- Used SQL CRUD operations for menu management.
- Added billing logic with quantity and total calculations.
