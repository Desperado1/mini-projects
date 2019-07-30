class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		currentnode = self
		while True:
			if value < currentnode.value:
				if currentnode.left is None:
					currentnode.left = BST(value)
					break
				else:
					currentnode = currentnode.left
			else:
				if currentnode.right is None:
					currentnode.right = BST(value)
					break
				else:
					currentnode = currentnode.right



        return self

    def contains(self, value):
        # Write your code here.
		currentnode = self
		while currentnode is not None:
			if currentnode.value > value:
				currentnode = currentnode.left
			elif currentnode.value < value:
				currentnode = currentnode.right
			else:
				return True
		return False

    def remove(self, value, parentnode = None):
        # Write your code here.
        # Do not edit the return statement of this method.
		currentnode = self

		while currentnode is not None:
			if currentnode.value > value:
				parentnode = currentnode
				currentnode = currentnode.left
			elif currentnode.value < value:
				parentnode = currentnode
				currentnode = currentnode.right
			else:
				if currentnode.left is not None and currentnode.right is not None:
					currentnode.value = currentnode.left.getmax()
					currentnode.left.remove(currentnode.value, currentnode)
				elif parentnode is None:
					if currentnode.left is not None:
						currentnode.value = currentnode.left.value
						currentnode.right = currentnode.left.right
						currentnode.left = currentnode.left.left
					if currentnode.right is not None:
						currentnode.value = currentnode.right.value
						currentnode.left = currentnode.right.left
						currentnode.right = currentnode.right.right
					else:
						currentnode.value = None
				elif parentnode.left == currentnode:
					parentnode.left = currentnode.left if currentnode.left is not None else currentnode.right
				elif parentnode.right == currentnode:
					parentnode.left = currentnode.left if currentnode.left is not None else currentnode.right
				break

        return self
	def getmax(self):
		currentnode = self
		while currentnode.right is not None:
			currentnode = currentnode.right
		return currentnode.value
	def getmin(self):
		currentnode = self
		while currentnode.left is not None:
			currentnode = currentnode.left
		return currentnode.value
