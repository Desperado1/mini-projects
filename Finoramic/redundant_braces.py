class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        braces = 0
        for i in A:
            if i == '(':
                braces += 1
            elif i in "+-/*":
                braces -= 1
            if braces < 0:
                braces = 0
        if braces == 0:
            return 0
        else:
            return 1