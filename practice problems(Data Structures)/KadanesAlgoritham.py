"""
input a non empty array of integers and returns the max sum possible
in a subarray and the subarray only contains adjacent numbers.
"""

def kadanesAlgorithm(array):
    # Write your code here.
	total = array[0]
	newTotal = array[0]
	for i in range(1, len(array)):
		newTotal = max(array[i], newTotal + array[i])
		total = max(total, newTotal)

	return total
