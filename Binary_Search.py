# Python Program for Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
x = 7

result = binary_search(arr, x)

if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found")
