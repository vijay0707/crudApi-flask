# Flask CRUD API

This is a simple CRUD (Create, Read, Update, Delete) API built using Flask and SQLAlchemy, allowing you to manage records in a PostgreSQL database. The Main purpose of this api is to build end to end ci/cd pipeline with all the necessary steps to spin up the application in cloud.

## Getting Started

To get started with the API, follow these instructions:

### Prerequisites

- Python 3.x
- PostgreSQL

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/flask-crud-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-crud-api
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your PostgreSQL database and update the connection details in `app.py`.

5. Run the Flask application:

    ```bash
    python app.py
    ```

The API will be accessible at http://localhost:5000.

## API Endpoints

The following endpoints are available:

- `POST /records`: Create a new record.
- `GET /records/<id>`: Retrieve a record by ID.
- `PUT /records/<id>`: Update an existing record by ID.
- `DELETE /records/<id>`: Delete a record by ID.

For detailed information on how to use each endpoint, refer to the Swagger documentation provided at http://localhost:5000/api/docs.

## Swagger Documentation

The API is documented using Swagger. You can access the Swagger documentation at http://localhost:5000/apidocs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
