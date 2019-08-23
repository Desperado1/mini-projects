"""
given a tree with the top element and two others find the youngest common ancestor of the two elements
"""


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	depthOne = getDescendantDepth(descendantOne, topAncestor)
	depthTwo = getDescendantDepth(descendantTwo, topAncestor)
	if depthOne > depthTwo:
		return backtrackAncestoralTree(descendentOne, descendantTwo, depthOne-depthTwo)
	else:
		return backtrackAncestoralTree(descendentTwo, descendantTwo, depthTwo-depthOne)

def getDescendantDepth(des, anc):
	depth = 0
	while des != ans:
		depth += 1
		des = des.ancestor
	return depth

def getAncestoralTree(lower, higher, diff):
	while diff > 0:
		diff -= 1
		lower = lower.ancestor
	while lower != higher:
		lower = lower.ancestor
		higher = higher.ancestor
	return lower
