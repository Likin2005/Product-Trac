# Product Trac

Product Trac is a product inventory management application with a React frontend and a FastAPI backend. It supports creating, viewing, updating, deleting, searching, and sorting products.

## Project structure

```text
FastAPI/
├── backend/
│   ├── database.py
│   ├── database_model.py
│   ├── main.py
│   └── models.py
├── frontend/
│   ├── public/
│   └── src/
├── .env
└── README.md
```

## Requirements

- Python 3.10 or newer
- Node.js and npm
- A database configured through `DATABASE_URL` in `.env`

## Configuration

Create a `.env` file in the project root and set the database connection string:

```env
DATABASE_URL=your-database-connection-string
```

Do not commit `.env` or database credentials to source control.

## Running the application

Run the backend and frontend in separate terminals.

### Backend

From the project root:

```powershell
.\venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload
```

The backend runs at `http://localhost:8000`.

Interactive API documentation is available at:

- `http://localhost:8000/docs`
- `http://localhost:8000/redoc`

### Frontend

From the `frontend` directory:

```powershell
npm install
npm start
```

The frontend runs at `http://localhost:3000` and uses the proxy configured in `frontend/package.json` to reach the backend.

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check that the backend is running |
| GET | `/products` | Retrieve all products |
| GET | `/products/{id}` | Retrieve a product by ID |
| POST | `/products` | Create a product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |

Product fields:

```json
{
  "id": 1,
  "name": "Example product",
  "description": "Product description",
  "price": 10.5,
  "quantity": 5
}
```

`id`, `price`, and `quantity` must be at least `1`.

## Troubleshooting

- Start the backend before loading the frontend.
- If the frontend cannot reach the API, verify that the backend is running on port `8000`.
- If the API documentation fails to load, start the backend with `uvicorn backend.main:app --reload` from the project root.
- If PowerShell blocks virtual-environment activation, run:

  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
