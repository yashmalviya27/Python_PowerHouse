# Bubble sorting implementation in Python.

# time complexity: O(n^2)
# space complexity: O(1)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr

# Selection sorting implementation in Python.

# time complexity: O(n^2)
# space complexity: O(1)
def selection_sort(arr):
    n = len(arr)-1
    for i in range(n):
        j = i+1
        min = i
        for k in range(j , n):
            if arr[min]>arr[k]:
                min = k
        arr[i],arr[min] = arr[min],arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selection_sort(arr)
print(sorted_arr)


