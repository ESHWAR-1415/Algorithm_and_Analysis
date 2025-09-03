# Insertion sort in Python
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


data = [45,32,16,84,76,1,19]
print(f"Original data: {data}")
insertionSort(data)
print(f"Sorted array: {data}")
