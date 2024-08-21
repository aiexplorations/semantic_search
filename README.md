# Semantic Search Application

This project is a semantic search application that leverages FastAPI for the backend, React for the frontend, and Qdrant for vector search. The application downloads books from Project Gutenberg, processes them, and allows users to perform semantic searches on the text content.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

- Download and process books from Project Gutenberg.
- Extract text content from downloaded books.
- Compute embeddings for text content using the BGE model.
- Store embeddings and text content in Qdrant.
- Perform semantic searches on the stored text content.
- User-friendly frontend interface for searching and displaying results.

## Architecture

The application consists of three main components:

1. **Backend**: Built with FastAPI, handles downloading, processing, and storing book data.
2. **Frontend**: Built with React, provides a user interface for searching and displaying results.
3. **Qdrant**: Vector search engine for storing and querying embeddings.

## Requirements

- Docker
- Docker Compose

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/semantic-search-app.git
cd semantic-search-app
```

### Run the app
```bash
docker-compose up
```
## Endpoints

## API Endpoints

The backend provides the following API endpoints:

- `GET /books`: Retrieves a list of all books in the database.
- `GET /books/{book_id}`: Retrieves a specific book by its ID.
- `POST /books`: Adds a new book to the database.
- `PUT /books/{book_id}`: Updates an existing book in the database.
- `DELETE /books/{book_id}`: Deletes a book from the database.

- `GET /search`: Performs a semantic search based on user input.
- `POST /embeddings`: Computes embeddings for a given text.

Please refer to the [API documentation](/workspaces/semantic_search/docs/api.md) for more details on each endpoint.

## Frontend

The frontend of the semantic search application is built using JavaScript (JS) and CSS. It leverages the React library to create a user-friendly interface for searching and displaying results.

The frontend components are organized in a modular and reusable manner, allowing for easy maintenance and scalability. The application utilizes modern JS features and best practices, such as functional components, hooks, and state management.

CSS is used to style the frontend components and create an appealing visual design. The application follows responsive design principles, ensuring that it looks and functions well on different screen sizes and devices.

In addition to React and CSS, the frontend may also utilize other libraries and frameworks for specific functionalities, such as data visualization or form handling.

Overall, the frontend of the semantic search application provides an intuitive and interactive user experience, enabling users to easily search for books and view the search results.

## Development

To contribute to the development of this project, follow these steps:

1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Start the backend server using `uvicorn main:app --reload`.
5. Start the frontend development server using `npm start`.
6. Make your changes and submit a pull request.


## Contributing
TBD

## License
TBD