# linear search implementation

def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# in ths i am usin divide and conquer approach for binary search implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(f"left: {left}, right: {right}")
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")