"""
taking array of positive integers as input and giving max sum possible  of
non-adjucent elememts in the array.
"""
def maxSubsetSumNoAdjacent(array):
	sum1 = 0
	maxsum = array[:]
	if not len(array):
		return 0
	if len(array) == 1:
		return array[0]
	maxsum[1] = max(array[0], array[1])
	for i in range(2, n+1):
		maxsum[i] = max(maxsum[i - 1], array[i] + maxsum[i - 2])
	return maxsum[-1]
