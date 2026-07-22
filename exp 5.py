import random

comparisons = 0


# Divide and Conquer Method
def min_max_dc(arr, low, high):
    global comparisons

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparisons += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    comparisons += 1
    minimum = left_min if left_min < right_min else right_min

    comparisons += 1
    maximum = left_max if left_max > right_max else right_max

    return minimum, maximum


# Simple Method
def min_max_normal(arr):

    minimum = arr[0]
    maximum = arr[0]

    count = 0

    for num in arr[1:]:

        count += 1
        if num < minimum:
            minimum = num

        count += 1
        if num > maximum:
            maximum = num

    return minimum, maximum, count


# Main Program

arr = [14, 3, 27, 9, 18, 5, 41, 11, 2, 30]

comparisons = 0

minimum, maximum = min_max_dc(arr, 0, len(arr) - 1)
dc_count = comparisons

_, _, normal_count = min_max_normal(arr)

print("Array :", arr)
print("Minimum Element :", minimum)
print("Maximum Element :", maximum)
print("Divide and Conquer Comparisons :", dc_count)
print("Normal Method Comparisons :", normal_count)


# Performance Analysis

print("\nPerformance Comparison")
print("------------------------------------------------")
print("Size\tDC\tNormal\tExpected")

sizes = [20, 50, 200, 1000]

for size in sizes:

    arr = [random.randint(1, 5000) for _ in range(size)]

    comparisons = 0

    min_max_dc(arr, 0, len(arr) - 1)
    dc = comparisons

    _, _, normal = min_max_normal(arr)

    expected = (3 * size) // 2 - 2

    print(size, "\t", dc, "\t", normal, "\t", expected)