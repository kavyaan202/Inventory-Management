# Inventory-Management

Inventory Management system built with Django and PostgreSQL, designed to help users track stock, manage product information, and handle transactions.

## Features

- User authentication and authorization.
- Add, update, and delete products.
- Stock management for inventory.
- View detailed inventory reports.
- Transaction tracking and history.
- Dynamic search for products.
- Responsive UI for better user experience.
  
## Technologies Used

- **Backend**: Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- Django 4.x
- PostgreSQL
- Pip (Python package installer)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kavyaan202/Inventory-Management.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Inventory-Management
   ```

3. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. **Install the Required Dependencies**:
   ```bash
   pip install django psycopg2
   ```

5. **Set up PostgreSQL Database**:

   Create a new PostgreSQL database and configure the database credentials in `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

6. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser** (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Navigate to `http://127.0.0.1:8000/` in your web browser.
2. Log in to access the inventory dashboard.
3. Use the admin panel (`http://127.0.0.1:8000/admin`) to manage products, stock, and users.

## Screenshots

![Inventory Dashboard](path-to-screenshot-1)

![Product Management](path-to-screenshot-2)

## Contributing

Feel free to fork this repository and submit pull requests. For significant changes, please open an issue to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out:

- **Email**: kavyanagaraj1111@gmail.com
- **GitHub**: [kavyaan202](https://github.com/kavyaan202)
