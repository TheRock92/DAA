import random
import time

# ---------- DETERMINISTIC QUICK SORT ----------
def deterministic_partition(arr, low, high):
    pivot = arr[high]   # Fixed pivot (last element)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)


# ---------- RANDOMIZED QUICK SORT ----------
def randomized_partition(arr, low, high):
    # Pick a random pivot and swap with last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)


# ---------- MAIN ----------
arr = [10, 7, 8, 9, 1, 5]
#user input: arr = list(map(int, input("Enter elements separated by space: ").split()))
print("Original array:", arr)

# Deterministic Quick Sort
det_arr = arr.copy()
start = time.time()
deterministic_quick_sort(det_arr, 0, len(det_arr) - 1)
end = time.time()
print("\nDeterministic Quick Sort result:", det_arr)
print("Time taken (sec):", round(end - start, 6))

# Randomized Quick Sort
rand_arr = arr.copy()
start = time.time()
randomized_quick_sort(rand_arr, 0, len(rand_arr) - 1)
end = time.time()
print("\nRandomized Quick Sort result:", rand_arr)
print("Time taken (sec):", round(end - start, 6))
