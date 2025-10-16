# Express Project

This is a simple Node.js Express project with a single `/me` endpoint. The project includes CORS support.

## Features

- Express-based web application.
- `/me` endpoint to return developer information and a cat fun fact.
- CORS enabled for cross-origin requests.

---

## Prerequisites

Before running this application, ensure you have the following installed:

- Node.js (v14+ recommended)
- `npm` (Node package manager)

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/busade/zero
    cd zero
    ```

2. Install dependencies:
    ```bash
    npm install express axios cors
    ```

---

## Usage

1. Run the application:
    ```bash
    node app.js
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:3000/me
    ```

---

## Endpoint

The app has only one endpoint `/me` and it will fetch a cat fun fact and return it with user information including email, current datetime, and stack.

### Example

```json
{
  "status": "success",
  "user": {
    "email": "adesolaisa3@gmail.com",
    "name": "Busari Adesola Issah",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-15T23:10:24.804Z",
  "fun_fact": "A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance."
}
```