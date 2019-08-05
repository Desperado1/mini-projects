"""
Finding three largest numbers from an array.
returning the leargest numbers as sorted array
"""

def findThreeLargestNumbers(array):
	new = [None, None, None]
    for num in array:
		updateLargest(new, num)
	return new

def updateLargest(array, num):
	if array[2] is None or num > array[2]:
		shift(num, array, 2)
	elif array[1] is None or num > array[1]:
		shift(num, array, 1)
	elif array[0] is None or num > array[0]:
		shift(num, array, 0)

def shift(num, array, idx):
	for i in range(idx + 1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i+1]
