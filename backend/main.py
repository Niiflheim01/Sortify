from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Literal, Optional
from sorting.algorithms import bubble_sort, merge_sort, quick_sort
from sorting.data_structures import Array, LinkedList

app = FastAPI(title="Sortify Sorting Simulator API")

class SortRequest(BaseModel):
    array: List[int]
    algorithm: Literal['bubble', 'merge', 'quick']
    data_structure: Optional[Literal['array', 'linked_list']] = 'array'

class SortStep(BaseModel):
    array: List[int]
    compare: Optional[List[int]] = None
    swap: Optional[List[int]] = None

class SortResponse(BaseModel):
    steps: List[SortStep]
    stats: dict

@app.post("/sort", response_model=SortResponse)
def sort_array(req: SortRequest):
    """
    Sort the input array using the selected algorithm and data structure.
    Returns the step-by-step process and statistics.
    """
    if req.data_structure == 'array':
        data = Array(req.array).to_list()
    elif req.data_structure == 'linked_list':
        data = LinkedList(req.array).to_list()
    else:
        raise HTTPException(status_code=400, detail="Invalid data structure.")

    if req.algorithm == 'bubble':
        steps, stats = bubble_sort(data)
    elif req.algorithm == 'merge':
        steps, stats = merge_sort(data)
    elif req.algorithm == 'quick':
        steps, stats = quick_sort(data)
    else:
        raise HTTPException(status_code=400, detail="Invalid algorithm.")

    # Convert steps to Pydantic models
    step_models = [SortStep(**step) for step in steps]
    return SortResponse(steps=step_models, stats=stats) 