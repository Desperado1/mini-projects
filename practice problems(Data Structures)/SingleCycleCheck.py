"""
given an array of integers, each integer respresents a jump of its value
in the array. return a boolean representing weather the jumps in the array
form a single cycle.starting at any index in the array and following the
jumps every element is visited exactly once before landing back on the
starting index.
"""


def hasSingleCycle(array):
    # Write your code here.
	numberOfElementsVisited = 0
	currentidx = 0
	while numberOfElementsVisited < len(array):
		if numberOfElementsVisited > 0 and currentidx == 0:
			return False
		numberOfElementsVisited += 1
		currentidx = nextElements(currentidx, array)
	return currentidx == 0

def nextElements(currentidx, array):
	jump = array[currentidx]
	idx = (currentidx + jump) % len(array)
	return idx if idx >= 0 else (idx + len(array))
	
