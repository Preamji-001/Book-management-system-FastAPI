Book Management System (BMS) API
Overview
This FastAPI-based API provides functionality for managing books in a Book Management System. It utilizes PostgreSQL as the database backend and connects to it using SQLAlchemy. Additionally, the project includes integration with pgAdmin4 for managing the PostgreSQL server.

Features
Authentication: Secured routes using JSON Web Tokens (JWT) for authentication.
CRUD Operations: Allows adding, retrieving, updating, and deleting book records.
PostgreSQL Database: Utilizes PostgreSQL for efficient data storage.
Session Management: Handles database sessions using SQLAlchemy.
Requirements
Python 3.7+
FastAPI
SQLAlchemy
PostgreSQL
pgAdmin4
Setting Up the Environment
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Set up PostgreSQL and create a database for the Book Management System. Update the DATABASE_URL in the main.py file accordingly.

Run the FastAPI server:

bash
Copy code
uvicorn main:app --reload
Database Management
The database sessions are managed through SQLAlchemy. The get_db function yields a session, and it's important to close the session after use. This is handled in the finally block.

Authentication
The API uses JWT-based authentication. Obtain an authentication token by making a POST request to the /auth endpoint with valid credentials.

Testing Documentation
The testign documentation for the given test cases and edge cases are provided in the app/test_case check it out for the testing documentation

API Documentation
The API documentation is available at http://localhost:8000/docs when the server is running. Use this interface to explore and test the available endpoints.

Bonus Points
To validate the authenticity of requests, a dedicated validation method/service has been implemented. This service checks the integrity and expiration of the JWT token, ensuring that only authorized users with valid tokens can interact with sensitive APIs. This two-step process adds an extra layer of security, safeguarding the API against unauthorized access and potential security threats.

This authentication/authorization system allows for fine-grained control over who can access different parts of the API, providing a secure and reliable environment for managing book-related operations.

Results
Check out the images section Under app to find about working of the data api and tested edge cases
