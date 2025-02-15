sample = [[0, 0], [0, 2], [1, 3], [2, 1]]

def second(x):
    return x[1]

print(sorted(sample, key=second)) # [[2, 1], [0, 2], [1, 3], [0, 4]]
print(sorted(sample, key=lambda x: x[1])  # [[2, 1], [0, 2], [1, 3], [0, 4]]

from functools import cmp_to_key

students = [
    ('kim', 'B+', 18),
    ('lee', 'A+', 21),
    ('jeong', 'A', 18),
]

def new_sort(n1, n2):
    if n1[2] > n2[2]: return 1
    elif n1[2] == n2[2]: return 0
    else: return -1

print(sorted(students, key=cmp_to_key(new_sort)))
print(sorted(students, key=lambda x: x[1] + str(x[2]), reverse=True))

# bubble sort
sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
def bubbleSort(data):
    for i in range(len(data) - 1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

bubbleSort(sample)
print(sample) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# selection sort
def selectionSort(data):
    for i in range(len(data)):
        idx = i
        for j in range(i + 1, len(data)):
            if data[idx] > data[j]:
                idx = j
        data[i], data[idx] = data[idx], data[i]
        
selectionSort(sample)
print(sample)


# insertion sort
def insertionSort(data):
    for end in range(1, len(data)):
        for i in range(end, 0, -1):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]

insertionSort(sample)
print(sample)

def insertionSort2(data):
    for idx in range(1, len(data)):
        i = idx
        while i > 0 and data[i - 1] > data[i]:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1

# quick sort
def quickSort(data, low, high):
    if low >= high:
        return  # Base case

    p = data[(low + high) // 2]  # Choose middle element as pivot
    left, right = low, high

    while left <= right:
        while data[left] < p:
            left += 1
        while data[right] > p:
            right -= 1
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1

    quickSort(data, low, right)   # Sort left side
    quickSort(data, left, high)   # Sort right side

arr = [34, 7, 23, 32, 5, 62, 32, 7]
quickSort(arr, 0, len(arr) - 1)
print(arr)
            
# merge sort
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result.extend([*left, *right])
    return result

def mergeSort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    return merge(left, right)

print(mergeSort(sample))

def merge(left, right):
    result = []
    i, j = 0, 0  # Pointers for left and right lists

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(data):
    if len(data) <= 1:
        return data  # Base case: already sorted

    mid = len(data) // 2
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    
    return merge(left, right)

# Example usage
sample = [34, 7, 23, 32, 5, 62, 32, 7]
print(mergeSort(sample))  # Output: [5, 7, 7, 23, 32, 32, 34, 62]

# tree sort
class Node:
    def __init__(self, item = 0):
        self.key = item
        self.left, self.right = None, None

root = Node()

def insert(root, key):
    if (root == None):
        root = Node(key)
        return root

    if (key < root.key):
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def treeinsert(data, root):
    for key in data:
        root = insert(root, key)

def inorderRec(root, answer):
    if root:
        inorderRec(root.left, answer)
        answer.append(root.key)
        inorderRec(root.right, answer)

treeinsert(sample, root)
inorderRec(root, answer)
print(answer[1:])

# heap sort
def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[i] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heapSort(data):
    n = len(data)
    for i in range(n, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

heapSort(sample)
print(sample)

from heapq import heappush, heappop

def heapSort(iterable):
    h = []
    for value in iterable: heappush(h, value)
    return [heappop(h) for i in range(len(h))]

print(heapSort(sample))
