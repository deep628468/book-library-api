# Book Library API

A RESTful Book Library API built with **Flask, PostgreSQL, and SQLAlchemy**. The application provides CRUD operations for managing books, with input validation, error handling, environment-based configuration, and a service-layer architecture.

## Features

* Create a new book
* Retrieve all books
* Retrieve a book by ID
* Update an existing book
* Delete a book
* Input validation for book data
* Error handling for invalid requests and missing resources
* PostgreSQL database integration
* SQLAlchemy ORM
* Service-layer architecture
* Environment-based database configuration
* API testing using cURL

## Technologies Used

* Python 3.13
* Flask 3.1.3
* Flask-SQLAlchemy 3.1.1
* SQLAlchemy 2.0.52
* PostgreSQL
* psycopg2-binary
* python-dotenv
* cURL
* Git and GitHub

## Project Architecture

The application follows a simple layered architecture:

```text
Client
  │
  ▼
Flask Routes
  │
  ▼
Service Layer
  │
  ▼
SQLAlchemy Model
  │
  ▼
PostgreSQL Database
```

### Responsibilities

* **Routes:** Handle HTTP requests, input validation, and HTTP responses.
* **Service Layer:** Handle database operations and application logic.
* **Models:** Define the database structure using SQLAlchemy.
* **Configuration:** Load environment-based application settings.
* **PostgreSQL:** Store persistent book data.

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
│       ├── __init__.py
│       └── book_service.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

> The `.env` file contains local configuration and should not be committed to GitHub. Use `.env.example` as a template.

## API Endpoints

| Method | Endpoint      | Description              |
| ------ | ------------- | ------------------------ |
| GET    | `/books`      | Retrieve all books       |
| GET    | `/books/<id>` | Retrieve a specific book |
| POST   | `/books`      | Create a new book        |
| PUT    | `/books/<id>` | Update an existing book  |
| DELETE | `/books/<id>` | Delete a book            |

## API Usage

### Get All Books

```bash
curl http://127.0.0.1:5001/books
```

### Get a Book by ID

```bash
curl http://127.0.0.1:5001/books/10
```

### Create a Book

```bash
curl -X POST http://127.0.0.1:5001/books \
-H "Content-Type: application/json" \
-d '{"title":"The Alchemist","author":"Paulo Coelho"}'
```

Example response:

```json
{
  "author": "Paulo Coelho",
  "id": 10,
  "title": "The Alchemist"
}
```

### Update a Book

```bash
curl -X PUT http://127.0.0.1:5001/books/10 \
-H "Content-Type: application/json" \
-d '{"title":"The Alchemist Updated","author":"Paulo Coelho"}'
```

### Delete a Book

```bash
curl -X DELETE http://127.0.0.1:5001/books/10
```

Example response:

```json
{
  "message": "Book deleted successfully"
}
```

## Input Validation

The API validates incoming book data before passing it to the service layer.

Validation includes:

* Title is required
* Author is required
* Title must be a non-empty string
* Author must be a non-empty string
* Leading and trailing whitespace is removed
* Invalid or missing data returns an HTTP `400` response

Example:

```json
{
  "title": "   ",
  "author": "Paulo Coelho"
}
```

Response:

```json
{
  "error": "Title must be a non-empty string"
}
```

## Error Handling

The API currently handles common errors including:

* `400 Bad Request` — invalid or missing request data
* `404 Not Found` — requested book does not exist

Example:

```json
{
  "error": "Book not found"
}
```

## Environment Configuration

The application uses environment variables for database configuration.

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/book_library
```

The actual database credentials should remain in `.env` and should not be committed to GitHub.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd book-library-api
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Configure the PostgreSQL connection in `.env`.

## Running the Application

Start the Flask application:

```bash
python run.py
```

The API will be available at:

```text
http://127.0.0.1:5001
```

Test the API:

```bash
curl http://127.0.0.1:5001/books
```

## Testing

The CRUD operations and validation/error-handling cases were tested using cURL.

Tested scenarios include:

* Retrieve all books
* Retrieve an existing book
* Retrieve a nonexistent book
* Create a valid book
* Reject invalid book data
* Update an existing book
* Reject invalid update data
* Update a nonexistent book
* Delete an existing book
* Delete a nonexistent book

## Current Status

The core REST API, PostgreSQL integration, CRUD functionality, input validation, service-layer architecture, and systematic API testing are complete.

### Remaining Development

* Final production configuration
* Docker containerization
* Production server configuration
* Cloud deployment
* Final security review

## License

This project is currently intended for educational and portfolio purposes.

