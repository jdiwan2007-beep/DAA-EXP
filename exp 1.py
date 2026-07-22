import time
import random


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and target >= arr[low] and target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            else:
                return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]

    print("\nPerformance Comparison")
    print("-----------------------------------------------")
    print("Size\tInterpolation(ms)\tBinary(ms)")

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        start = time.time()
        for i in range(100):
            index1, comp1 = interpolation_search(arr, target)
        inter_time = (time.time() - start) / 100 * 1000

        start = time.time()
        for i in range(100):
            index2, comp2 = binary_search(arr, target)
        binary_time = (time.time() - start) / 100 * 1000

        print(size, "\t", round(inter_time, 4), "\t\t", round(binary_time, 4))

        print("Interpolation Comparisons:", comp1)
        print("Binary Comparisons:", comp2)
        print()


# Main Program

arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

index, comparisons = interpolation_search(arr, target)

print("Array =", arr)
print("Target =", target)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

print("Comparisons =", comparisons)

performance_analysis()