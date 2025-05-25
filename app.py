from flask import Flask, render_template, jsonify, request
import random
import time
from typing import List, Dict

app = Flask(__name__)

class SortingVisualizer:
    def __init__(self):
        self.array = []
        self.array_size = 20
        self.comparisons = 0
        self.swaps = 0
        self.start_time = 0
        self.steps = []

    def generate_new_array(self):
        self.array = [random.randint(10, 100) for _ in range(self.array_size)]
        self.comparisons = 0
        self.swaps = 0
        self.steps = []
        return self.array

    def bubble_sort(self, arr):
        self.steps = []
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if arr[j] > arr[j + 1]:
                    self.swaps += 1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.steps.append({
                        'array': arr.copy(),
                        'comparing': [j, j + 1],
                        'sorted': list(range(n - i, n))
                    })
        return self.steps

    def merge_sort(self, arr):
        self.steps = []
        self._merge_sort_helper(arr, 0)
        return self.steps

    def _merge_sort_helper(self, arr, start_idx):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self._merge_sort_helper(arr[:mid], start_idx)
        right = self._merge_sort_helper(arr[mid:], start_idx + mid)

        return self._merge(left, right, start_idx)

    def _merge(self, left, right, start_idx):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                self.swaps += 1
            
            self.steps.append({
                'array': result.copy(),
                'comparing': [start_idx + i, start_idx + j],
                'sorted': []
            })

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def quick_sort(self, arr):
        self.steps = []
        self._quick_sort_helper(arr, 0, len(arr) - 1)
        return self.steps

    def _quick_sort_helper(self, arr, low, high):
        if low < high:
            pivot_idx = self._partition(arr, low, high)
            self._quick_sort_helper(arr, low, pivot_idx - 1)
            self._quick_sort_helper(arr, pivot_idx + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1
                self.steps.append({
                    'array': arr.copy(),
                    'comparing': [i, j, high],
                    'sorted': []
                })

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        self.steps.append({
            'array': arr.copy(),
            'comparing': [i + 1, high],
            'sorted': []
        })
        return i + 1

visualizer = SortingVisualizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    array = visualizer.generate_new_array()
    return jsonify({'array': array})

@app.route('/api/sort', methods=['POST'])
def sort():
    data = request.get_json()
    array = data.get('array', [])
    algorithm = data.get('algorithm', 'bubble')
    
    visualizer.comparisons = 0
    visualizer.swaps = 0
    visualizer.start_time = time.time()
    
    if algorithm == 'bubble':
        steps = visualizer.bubble_sort(array.copy())
    elif algorithm == 'merge':
        steps = visualizer.merge_sort(array.copy())
    elif algorithm == 'quick':
        steps = visualizer.quick_sort(array.copy())
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400
    
    return jsonify({
        'steps': steps,
        'stats': {
            'comparisons': visualizer.comparisons,
            'swaps': visualizer.swaps,
            'time': time.time() - visualizer.start_time
        }
    })

if __name__ == '__main__':
    app.run(debug=True) 