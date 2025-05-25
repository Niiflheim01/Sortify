import time


def bubble_sort(arr):
    n = len(arr)
    steps = []
    comparisons = 0
    swaps = 0
    start_time = time.time()
    a = arr[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            steps.append({'array': a[:], 'compare': [j, j+1], 'swap': None})
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                steps.append({'array': a[:], 'compare': [j, j+1], 'swap': [j, j+1]})
    elapsed = time.time() - start_time
    return steps, {'comparisons': comparisons, 'swaps': swaps, 'time': elapsed}


def merge_sort(arr):
    steps = []
    comparisons = [0]
    swaps = [0]
    start_time = time.time()
    a = arr[:]

    def merge(left, right, l_idx):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            steps.append({'array': a[:], 'compare': [l_idx + i, l_idx + len(left) + j], 'swap': None})
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                swaps[0] += 1
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(sub, l_idx):
        if len(sub) <= 1:
            return sub
        mid = len(sub) // 2
        left = sort(sub[:mid], l_idx)
        right = sort(sub[mid:], l_idx + mid)
        merged = merge(left, right, l_idx)
        a[l_idx:l_idx+len(merged)] = merged
        steps.append({'array': a[:], 'compare': None, 'swap': None})
        return merged

    sort(a, 0)
    elapsed = time.time() - start_time
    return steps, {'comparisons': comparisons[0], 'swaps': swaps[0], 'time': elapsed}


def quick_sort(arr):
    steps = []
    comparisons = [0]
    swaps = [0]
    start_time = time.time()
    a = arr[:]

    def partition(low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            steps.append({'array': a[:], 'compare': [j, high], 'swap': None})
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps[0] += 1
                steps.append({'array': a[:], 'compare': [i, j], 'swap': [i, j]})
        a[i+1], a[high] = a[high], a[i+1]
        swaps[0] += 1
        steps.append({'array': a[:], 'compare': [i+1, high], 'swap': [i+1, high]})
        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(a) - 1)
    elapsed = time.time() - start_time
    return steps, {'comparisons': comparisons[0], 'swaps': swaps[0], 'time': elapsed} 