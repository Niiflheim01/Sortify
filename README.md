# Sortify - Space-Themed Sorting Algorithm Visualizer

A beautiful, space-themed visualization tool for understanding sorting algorithms. Watch as different sorting algorithms work their magic on arrays of numbers, with real-time statistics and a stunning space-themed interface.

## Features

- Visualize three different sorting algorithms:
  - Bubble Sort
  - Merge Sort
  - Quick Sort
- Real-time statistics:
  - Number of comparisons
  - Number of swaps
  - Time taken
- Interactive controls:
  - Generate new random arrays
  - Choose different sorting algorithms
  - Pause/Resume sorting
- Space-themed UI with animated stars and color-coded bars

## Requirements

- Python 3.7+
- Pygame
- NumPy

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

Simply run:
```bash
python sortify.py
```

## How to Use

1. Click "Generate" to create a new random array
2. Choose a sorting algorithm by clicking one of the algorithm buttons
3. Watch the visualization and statistics in real-time
4. Use the "Pause" button to pause/resume the sorting process
5. Generate a new array at any time to start over

## Controls

- **Generate**: Creates a new random array
- **Bubble Sort**: Starts bubble sort visualization
- **Merge Sort**: Starts merge sort visualization
- **Quick Sort**: Starts quick sort visualization
- **Pause**: Pauses/resumes the current sorting process

## Color Coding

- Blue bars: Unsorted elements
- Orange bars: Elements being compared
- Green bars: Sorted elements

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