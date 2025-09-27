🐾 Vet Connect

Vet Connect is a web application designed to connect pet owners with veterinary services. The platform provides an easy way for users to manage appointments times, store pet information, and communicate with veterinary professionals.

🚀 Features

User authentication (sign up, log in)

Pet information management (name, breed)

Appointment scheduling

Responsive design with Bootstrap

Data persistence with SQL database

Backend powered by Django

🛠️ Technologies Used

Backend: Django (Python)

Database: SQL (PostgreSQL)

Frontend: HTML, CSS, Bootstrap, Javascript

Other Tools: Git, VS Code

⚙️ Installation

Follow these steps to set up the project locally:

Clone the repository

git clone https://github.com/your-username/vet-connect.git
cd vet-connect


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
pipenv shell # Activate virtual Enviroment in MacOs.

Install dependencies 

pip install psycopg2-binary


Run database migrations(make the migrations)

python manage.py migrate


Start the development server

python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/appointments/




![alt text](../appointments/templates/static/images/projects5.png)


📂 Project Structure

vet-connect/
│── migrations/                     # Migration files for database changes
│
├── appointments/                   # App for handling appointments
│   ├── templates/                   # HTML templates (Bootstrap, CSS, JS)
│   │   ├── admin_appointment.html
│   │   ├── appointments_index.html  # Home page
│   │   ├── book_appointment.html
│   │   ├── login.html
│   │   ├── my_appointment.html
│   │   └── register.html
│   │
│   ├── static/images/               # Static files (images, CSS, JS)
│   │
│   ├── __init__.py
│   ├── admin.py                     # Customize and register models with Django admin site
│   ├── apps.py                      # App configuration
│   ├── forms.py                     # Create forms
│   ├── models.py                    # Database models (migrations to SQL)
│   ├── tests.py                     # Test cases
│   ├── urls.py                      # Routes for the appointments app
│   └── views.py                     # Connect backend with frontend
│
├── vetconnect/                      # Main project configuration folder
│   ├── __init__.py
│   ├── settings.py                  # Project settings
│   ├── urls.py                      # Root routes, includes appointments app URLs
│   └── wsgi.py                      # WSGI entry point
│
├── db.sqlite3                       # Default SQLite database
├── manage.py                        # Django management script
└── requirements.txt                 # Python dependencies


🤝 Contributing

Contributions are welcome! To contribute:

Fork the repo

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push to your branch (git push origin feature-name)

Create a Pull Request

📜 License

This project is licensed under the Apache-2.0 license.
