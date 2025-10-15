# FastAPI Project

This is a simple FastAPI project with a single `/` endpoint. The project also includes CORS support and auto-generated documentation.

## Features

- FastAPI-based web application.
- `/` endpoint to return developer information.
- Automatically generated Swagger and ReDoc documentation.
- CORS enabled for cross-origin requests.

---

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7+
- `pip` (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/busade/zero
   cd zero

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/scripts/activate  #on cmd env\scripts\activate

3. Install dependencies
    ```bash
    pip install -r requirements.txt


## Usage
1. Run the Application
    ```bash
    fastapi dev main.py
2. Open your browser and navigate to
    Swagger UI: http://127.0.0.1:8000/docs


## Endpoint
The app has only one endpoint /me and it will fetch a cat fun fact and return with user information inluding email, current datetime and stack

### Example
`code
   {
    "status": "success",
    "user": {
        "email": "adesolaisa3@gmail.com",
        "name": "Busari Adesola Issah",
        "stack": "Python/Flask"
    },
    "timestamp": "2025-10-15T23:10:24.804534Z",
    "fun_fact": "A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance."
}
`
