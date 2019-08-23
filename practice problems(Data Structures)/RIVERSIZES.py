"""
given a 2d array of values 0 and 1. 0 determines land and 1 determines land. number of adjacent 1s(not digonal)
determines the size of the river. output an array that shows the sizes of rivers.
"""


def riverSizes(matrix):
    # Write your code here.
	visited = [[False for value in row] for row in matrix]
	sizes = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:
				continue
			traverseNode(i, j, matrix, visited, sizes)
	return sizes

def traverseNode(i, j, matrix, visited, sizes ):
	currentRiverSize = 0
	nodesToExplore = [[i, j]]
	while len(nodesToExplore):
		currentnode = nodesToExplore.pop(0)
		i = currentnode[0]
		j = currentnode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		currentRiverSize += 1
		unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visited)
		for neighbour in unvisitedNeighbours:
			nodesToExplore.append(neighbour)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)

def getUnvisitedNeighbours(i, j, matrix, visited):
	unvisitedNeighbours = []
	if i > 0 and not visited[i-1][j]:
		unvisitedNeighbours.append([i-1, j])
	if i < len(matrix) - 1 and not visited[i+1][j]:
		unvisitedNeighbours.append([i+1, j])
	if j > 0 and not visited[i][j-1]:
		unvisitedNeighbours.append([i, j-1])
	if j < len(matrix[0])-1 and not visited[i][j+1]:
		unvisitedNeighbours.append([i, j+1])
	return unvisitedNeighbours
