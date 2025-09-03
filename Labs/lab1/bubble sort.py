# Bubble sort in Python
def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        
        array[j], array[j+1] = array[j+1], array[j]
        

data = [45,32,16,84,76,1,19]
print(f"Original data: {data}")
bubbleSort(data)
print('Sorted Array: ',data)
