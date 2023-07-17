# internshipproject
For internship purpose only
# I had to be honest, i ask help from chatgpt because i need to prepare for exam those.
# If i have more free time, i can modify and make the page perfectly include with css, more well-done and secure function.

This project implements a simple login system with a backend server using FastAPI. It allows users to log in with a username and password, and provides token-based authentication using JSON Web Tokens (JWT). The backend server is built with FastAPI, and a basic frontend is included to demonstrate the login functionality.


Features
-User login with username and password
-Token-based authentication using JWT
-SQLite database for login tracking
-Simple HTML frontend

Prerequisites
-Python 3.7 or higher
-pip package manager

Installation
##Clone the repository:##
git clone <repository-url>

##Navigate to the project directory:##
  cd login-system-fastapi

##Create a virtual environment (On Windows):##
  python -m venv venv
  venv\Scripts\activate

##On macOS and Linux:##
  python3 -m venv venv
  source venv/bin/activate

##Install the required packages:##
  pip install -r requirements.txt

Usage
1) Start the backend server:
view command

2) Open the index.html file in a web browser.
The frontend login form will be displayed. Enter a username and password, and click the "Login" button. If the login is successful, you will be redirected to a protected route.

Additional Notes
- The SQLite database file (login.db) will be created automatically when the server starts if it doesn't already exist. It will store the login information.
- For demonstration purposes, a simple secret key ("secret_key") is used for JWT token signing. In a production environment, make sure to replace it with a strong and secure secret key.
- The requirements.txt file lists all the packages used in the project. It's recommended to use a virtual environment to isolate the project dependencies and ensure a clean environment.
