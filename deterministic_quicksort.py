def quicksort(arr):
    if len(arr) <= 1:  # If the list has 1 or no elements, it's already sorted
        return arr
    pivot = arr[-1]  # Pick the last element as the pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements smaller or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements larger than pivot
    return quicksort(left) + [pivot] + quicksort(right)  # Sort left, pivot, and right

# Example usage
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array =  quicksort(array)
print(f"Original: {array}")
print(f"Sorted: {sorted_array}")