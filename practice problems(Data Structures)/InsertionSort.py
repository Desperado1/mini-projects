def insertionSort(array):
    # Write your code here.
	n = len(array)
	for i in range(1, n):
		j = i - 1
		key = array[i]
		while j >= 0 and key < array[j]:
			array[j+1] = array[j]
			j -= 1
		array[j + 1] = key
	return array
