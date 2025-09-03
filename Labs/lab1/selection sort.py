def selectionSort(array, n):
    for step in range(n):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [45,32,16,84,76,1,19]
print(f"Original data: {data}")
size = len(data)
selectionSort(data, size)
print("Sorted Array :",data)
