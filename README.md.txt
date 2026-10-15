# FastAPI CRUD Notes Application with JWT Authentication

A backend REST API application developed using **Python, FastAPI, PostgreSQL, SQLAlchemy, and JWT Authentication**.

This project demonstrates secure user authentication and CRUD (Create, Read, Update, Delete) operations for managing personal notes.

## Project Overview

The FastAPI CRUD Notes Application is designed to demonstrate backend development concepts such as database integration, authentication, authorization, and REST API operations.

Users can register, log in, receive JWT access tokens, and manage notes through protected API endpoints.

The application uses PostgreSQL for data storage and SQLAlchemy ORM for database operations.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- JWT Authentication
- Passlib (Password Hashing)
- Uvicorn
- Swagger UI
- Visual Studio Code

## Key Features

### User Authentication
- User registration
- User login
- Password hashing
- JWT access token generation
- Token-based authentication
- Protected API endpoints

### Notes Management
- Create new notes
- Retrieve all notes
- Retrieve a specific note
- Update existing notes
- Delete notes
- Associate notes with users

### Database Integration
- PostgreSQL database connection
- SQLAlchemy ORM models
- User and Notes tables
- Primary and foreign key relationships
- Database session management

## Project Structure

```text
fastapi-jwt-crud-notes-app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate user and generate JWT |
| GET | `/notes` | Retrieve notes |
| POST | `/notes` | Create a new note |
| GET | `/notes/{note_id}` | Retrieve a note by ID |
| PUT | `/notes/{note_id}` | Update a note |
| DELETE | `/notes/{note_id}` | Delete a note |

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-jwt-crud-notes-app.git
```

### Step 2: Open the Project Folder

```bash
cd fastapi-jwt-crud-notes-app
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic passlib bcrypt python-jose python-multipart
```

### Step 6: Configure PostgreSQL

Create a PostgreSQL database named:

```sql
CREATE DATABASE crud_db;
```

Configure the database connection in `database.py` using your local PostgreSQL credentials.

**Security Note:** Keep database passwords and JWT secret keys outside public source code. Use environment variables before publishing the project.

### Step 7: Run the Application

```bash
uvicorn main:app --reload
```

### Step 8: Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Authentication Workflow

1. Register a new user using `/register`.
2. Log in using `/login`.
3. Receive a JWT access token.
4. Click the **Authorize** button in Swagger UI.
5. Authenticate using the token.
6. Access protected Notes API endpoints.

## Example: Create a Note

**Request**

```http
POST /notes
```

**JSON Body**

```json
{
  "title": "Shopping",
  "content": "Milk"
}
```

**Example Response**

```json
{
  "id": 3,
  "title": "Shopping",
  "content": "Milk"
}
```

## Example: Update a Note

**Request**

```http
PUT /notes/3
```

**JSON Body**

```json
{
  "title": "Shopping",
  "content": "Milk & Curd"
}
```

## Error Handling

The application demonstrates HTTP error handling.

- **200 OK** – Successful API request
- **400 Bad Request** – Duplicate username
- **401 Unauthorized** – Invalid authentication credentials
- **404 Not Found** – Requested note not found

## API Testing

The APIs were tested using Swagger UI.

The project screenshots demonstrate:

- Duplicate username validation
- Successful login and JWT token generation
- Successful note creation
- Successful note update
- Note deletion request and 404 response for a missing note

## Learning Outcomes

Through this project, I gained practical experience in:

- Building REST APIs with FastAPI
- Implementing JWT authentication
- Hashing and verifying passwords
- Integrating PostgreSQL with SQLAlchemy
- Designing database models and relationships
- Performing CRUD operations
- Handling HTTP errors
- Testing protected API endpoints with Swagger UI

## Future Enhancements

- Automated unit and integration tests
- Environment-based configuration
- Refresh token support
- Pagination and filtering
- Docker containerization
- Cloud deployment

## Author

**Gowtham M**

Python | FastAPI | PostgreSQL | Backend Development | Generative AI

## Project Status

**Backend CRUD Application – Development and API Testing**