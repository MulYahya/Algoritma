import random

# Generate random integers
def generate_random_numbers(seed, size, min_val, max_val):
    random.seed(seed)
    return [random.randint(min_val, max_val) for _ in range(size)]

# Conquer sorting (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive sorting
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
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

    # Sort using Merge Sort
    merge_sorted = merge_sort(random_numbers.copy())
    print("Sorted with Merge Sort:", merge_sorted)
