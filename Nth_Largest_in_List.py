# Find N largest elements from a list
import heapq

arr = [5, 1, 9, 3, 7, 6, 8]
N = 3

largest_elements = heapq.nlargest(N, arr)

print("The", N, "largest elements are:", largest_elements)
