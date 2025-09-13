#Break a list into chunks of size N
def chunk_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3
chunks = chunk_list(my_list, n)
print("Chunks:", chunks)
