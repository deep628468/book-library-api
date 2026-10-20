# Book Library API

A RESTful Book Library API built with **Flask, PostgreSQL, and SQLAlchemy**. The application supports CRUD operations for managing books, input validation, error handling, environment-based configuration, and a service-layer architecture.

**Live API:** https://book-library-api-dsc2.onrender.com

**GitHub Repository:** https://github.com/deep628468/book-library-api

## Features

- Create, retrieve, update, and delete books
- Retrieve all books or a specific book by ID
- Input validation for book data
- Error handling for invalid requests and missing resources
- PostgreSQL database integration
- SQLAlchemy ORM
- Service-layer architecture
- Environment-based database configuration
- Docker containerization
- Cloud deployment on Render
- API testing using cURL

## Technologies Used

- Python 3.13
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- PostgreSQL
- psycopg2-binary
- python-dotenv
- Docker
- Gunicorn
- cURL
- Git and GitHub
- Render

## Project Architecture

The application follows a layered architecture:

```text
Client
  |
  v
Flask Routes
  |
  v
Service Layer
  |
  v
SQLAlchemy Models
  |
  v
PostgreSQL Database
```

### Responsibilities

- **Routes:** Handle HTTP requests, input validation, and HTTP responses.
- **Service Layer:** Manage database operations and application logic.
- **Models:** Define the database structure using SQLAlchemy.
- **Configuration:** Load application settings from environment variables.
- **PostgreSQL:** Store book records persistently.

## Project Structure

```text
book-library-api/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py
│   └── services/
│       ├── __init__.py
│       └── book_service.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.py
└── README.md
```

The `.env` file contains local configuration and must not be committed to GitHub. Use `.env.example` as a template.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check application health |
| GET | `/books` | Retrieve all books |
| GET | `/books/<id>` | Retrieve a book by ID |
| POST | `/books` | Create a new book |
| PUT | `/books/<id>` | Update an existing book |
| DELETE | `/books/<id>` | Delete a book |

## API Usage

The following examples use the deployed API. You can replace the base URL with `http://127.0.0.1:5001` when testing locally.

### 1. Health Check

```bash
curl -i https://book-library-api-dsc2.onrender.com/health
```

### 2. Retrieve All Books

```bash
curl https://book-library-api-dsc2.onrender.com/books
```

### 3. Retrieve a Book by ID

```bash
curl -i https://book-library-api-dsc2.onrender.com/books/1
```

### 4. Create a Book

```bash
curl -X POST https://book-library-api-dsc2.onrender.com/books \
  -H "Content-Type: application/json" \
  -d '{"title":"The Alchemist","author":"Paulo Coelho"}'
```

Example response:

```json
{
  "author": "Paulo Coelho",
  "id": 1,
  "title": "The Alchemist"
}
```

The returned ID is assigned by the database and may differ from this example.

### 5. Update a Book

```bash
curl -X PUT https://book-library-api-dsc2.onrender.com/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"The Alchemist Updated","author":"Paulo Coelho"}'
```

### 6. Delete a Book

```bash
curl -i -X DELETE https://book-library-api-dsc2.onrender.com/books/1
```

Use an existing book ID when performing update or delete operations.

## Input Validation

The API validates incoming book data before passing it to the service layer.

Validation includes:

- Title is required.
- Author is required.
- Title and author must be non-empty strings.
- Leading and trailing whitespace is removed.
- Invalid or missing data returns an HTTP `400 Bad Request` response.

Example invalid request:

```json
{
  "title": "   ",
  "author": "Paulo Coelho"
}
```

Example error response:

```json
{
  "error": "Title must be a non-empty string"
}
```

## Error Handling

The API handles common request errors.

| Status Code | Meaning |
|---|---|
| `400 Bad Request` | Invalid or missing request data |
| `404 Not Found` | Requested book does not exist |
| `500 Internal Server Error` | Unexpected server-side error, if encountered |

Example: request a nonexistent book.

```bash
curl -i https://book-library-api-dsc2.onrender.com/books/999999
```

Verified response:

```http
HTTP/2 404
content-type: application/json
```

```json
{
  "error": "Book not found"
}
```

## Environment Configuration

The application uses environment variables for database configuration.

Create a `.env` file in the project root and configure your PostgreSQL connection:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/book_library
```

Replace the example credentials and database name with your actual local PostgreSQL configuration.

Never publish real database credentials, API keys, or production connection strings.

## Installation

Clone the repository:

```bash
git clone https://github.com/deep628468/book-library-api.git
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

Configure PostgreSQL and the `DATABASE_URL` environment variable before starting the application.

## Running Locally

Start the application:

```bash
python run.py
```

The local API is available at:

```text
http://127.0.0.1:5001
```

Test the API:

```bash
curl http://127.0.0.1:5001/books
```

## Docker

The application includes a `Dockerfile` and Docker Compose configuration for containerized execution.

To start the application using Docker Compose:

```bash
docker compose up --build
```

To stop the containers:

```bash
docker compose down
```

Configure the required environment variables before starting the containers. Database persistence and container behavior depend on the Docker Compose configuration.

## Deployment

The application is deployed on Render using Docker and Gunicorn, with PostgreSQL for persistent data storage.

- **Live API:** https://book-library-api-dsc2.onrender.com
- **Health Check:** https://book-library-api-dsc2.onrender.com/health
- **Books Endpoint:** https://book-library-api-dsc2.onrender.com/books

The deployment uses environment-based configuration for database connectivity.

## Testing

CRUD operations have been tested using cURL.

Testing scenarios include:

- Retrieve all books
- Retrieve an existing book
- Create a book
- Update an existing book
- Delete an existing book
- Request a nonexistent book and verify the `404 Not Found` response

Additional validation and error-handling tests should be run whenever the application changes.

## Current Status

- Flask REST API implemented
- PostgreSQL integration completed
- CRUD operations implemented and tested
- Input validation and error handling implemented
- Service-layer architecture implemented
- Docker containerization completed
- Application deployed on Render
- GitHub repository synchronized
- Nonexistent book ID handling verified

## License

This project is intended for educational and portfolio purposes. No formal open-source license has been specified.