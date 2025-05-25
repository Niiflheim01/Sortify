# Sortify

A visual sorting algorithm simulator for students and developers.

## Backend (Python FastAPI)

### Setup

1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### API Endpoint

- `POST /sort`
  - Request JSON:
    ```json
    {
      "array": [5, 2, 9, 1],
      "algorithm": "bubble", // or "merge", "quick"
      "data_structure": "array" // or "linked_list"
    }
    ```
  - Response JSON:
    ```json
    {
      "steps": [
        {"array": [5,2,9,1], "compare": [0,1], "swap": null},
        ...
      ],
      "stats": {"comparisons": 6, "swaps": 3, "time": 0.001}
    }
    ``` 