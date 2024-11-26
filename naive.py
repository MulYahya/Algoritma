import random

# Generate random integers
def generate_random_numbers(seed, size, min_val, max_val):
    random.seed(seed)
    return [random.randint(min_val, max_val) for _ in range(size)]

# Naive sorting (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Main program
if __name__ == "__main__":
    # Generate random numbers
    seed = 40
    size = 50
    min_val = 0
    max_val = 100
    random_numbers = generate_random_numbers(seed, size, min_val, max_val)
    print("Original Random Numbers:", random_numbers)

    # Sort using Bubble Sort
    bubble_sorted = bubble_sort(random_numbers.copy())
    print("Sorted with Bubble Sort:", bubble_sorted)
