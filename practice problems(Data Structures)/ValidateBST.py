def validateBst(tree):
    # Write your code here.
	return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minvalue, maxvalue):
	if tree is None:
		return True
	if tree.value < minvalue or tree.value >= maxvalue:
		return False
	leftIsValid = validateBstHelper(tree.left, minvalue, tree.value)
	return leftIsValid and validateBstHelper(tree.right, tree.value, maxvalue)
