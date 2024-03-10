# Restaurant Management System

This project aims to develop a comprehensive Restaurant Management System to streamline various operations within a restaurant, including table management, menu management, order management, and employee management.

## Features

- **Table Management**: Allows managing restaurant tables including assigning capacities and tracking availability.
- **Menu Management**: Facilitates the creation and management of menu items and categories.
- **Order Management**: Enables placing and tracking orders, managing order items, and calculating total amounts.
- **Employee Management**: Provides functionalities for managing employees such as waiters and receptionists.

## Components

### Authentication App

Handles user authentication for accessing the system.

### Table Management App

Manages restaurant tables including their numbers, capacities, and availability status.

### Menu Management App

Manages the menu items offered by the restaurant, including categories, item names, prices, and descriptions.

### Order Management App

Facilitates order placement, tracking, and management including table association, ordered items, total amounts, and order status.

### Employee Management App

Manages restaurant employees including waiters and receptionists, handling their personal information, contact details, shifts, and employment status.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure database settings in `settings.py`.

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Technologies Used

- **Django**: Python web framework for building robust web applications.
- **Django REST Framework**: A powerful toolkit for building Web APIs in Django.
- **SQLite**: A lightweight relational database used for development purposes.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or new features.

## License

This project is licensed under the [MIT License](LICENSE).
