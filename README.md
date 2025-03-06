# Book Store API

This is a FastAPI-based Book Store API that allows users to manage books with role-based access control. It includes features for authentication, role-based authorization, and CRUD operations for books.

## Features

- **Public Access**: Anyone can view the list of books.
- **Authentication**: Users must log in to access protected endpoints.
- **Role-Based Access Control**:
  - **Reader**: Can view books.
  - **Author**: Can create, update, and delete their own books.
  - **Admin**: Can view all books (future scope).
- **In-Memory Storage**: Data is stored in memory (for demonstration purposes).

## API Endpoints

### Authentication
- **POST /token**: Get an access token by providing username and password.

### Books
- **GET /api/v1/books**: Get a list of all books (public access).
- **GET /api/v1/books/{book_id}**: Get details of a specific book (requires authentication).
- **POST /api/v1/books**: Create a new book (requires author role).
- **PATCH /api/v1/books/{book_id}**: Update a book (requires author role and ownership).
- **DELETE /api/v1/books/{book_id}**: Delete a book (requires author role and ownership).

## User Credentials

| Username      | Password     | Role   |
|---------------|--------------|--------|
| `author_user` | `authorpass` | Author |
| `reader_user` | `readerpass` | Reader |
| `admin_user`  | `adminpass`  | Admin  |

## Installation

1. Clone the repository:
  ```bash
   git clone https://github.com/ichbingautam/book-store-api.git
   cd book-store-api
  ```
2. Install dependencies:
  ```bash
    pip3 install -r requirements.txt
  ````
3. Run the application:
  ```
    python3 -m uvicorn app.main:app --reload
    or python3 main.py
  ```

## Example Requests
1. Get Access Token
  ```bash
    curl -X POST "http://127.0.0.1:8000/token" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "username=author_user&password=authorpass"
  ```

2. Create a Book (Author Only)
  ```bash
    curl -X POST "http://127.0.0.1:8000/api/v1/books" \
      -H "Authorization: Bearer <access_token>" \
      -H "Content-Type: application/json" \
      -d '{"title": "New Book", "description": "A great book!"}'
  ```
3. Get All Books (Public)
  ```bash
    curl -X GET "http://127.0.0.1:8000/api/v1/books"
  ```
4. Update a Book (Author Only)
  ```bash
    curl -X PATCH "http://127.0.0.1:8000/api/v1/books/1" \
      -H "Authorization: Bearer <access_token>" \
      -H "Content-Type: application/json" \
      -d '{"title": "Updated Title"}'
  ```
5. Delete a Book (Author Only)
  ```bash
    curl -X DELETE "http://127.0.0.1:8000/api/v1/books/1" \
      -H "Authorization: Bearer <access_token>"
  ```
