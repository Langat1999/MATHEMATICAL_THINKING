#Randomized quicksort chooses a random pivot each time to improve average-case performance
#By randomly picking a pivot, this version of quicksort avoids pathological cases that can occur in traditional quicksort, demonstrating how randomness can be harnessed to improve performance
import random

def randomized_quicksort(arr):
    """Sorts an array using the randomized quicksort algorithm."""
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Randomly select a pivot

    # Partition the array into three sublists
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recursively sort the sublists and combine
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Generate a random unsorted list
unsorted_array = [random.randint(1, 100) for _ in range(10)]

print("Unsorted:", unsorted_array)
print("Sorted:", randomized_quicksort(unsorted_array))