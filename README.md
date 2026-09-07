# Book Library API

A RESTful Book Library API built using Flask, PostgreSQL, and SQLAlchemy. The API provides complete CRUD operations for managing books, along with basic error handling and input validation.

## Features

- Create a new book
- Retrieve all books
- Retrieve a book by ID
- Update an existing book
- Delete a book
- Error handling for invalid requests
- Input validation
- PostgreSQL database integration
- Environment-based database configuration

## Technologies Used

- Python 3.13
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- PostgreSQL
- psycopg2
- python-dotenv
- cURL for API testing

## Project Structure

```text
book-library-api/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py
│   │
│   └── services/
│       └── __init__.py
│
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
