class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        import sys
        mindiff = sys.maxsize
        A = sorted(A)
        length = len(A)
        for i in range(length-2):
            j = i+1
            k = length-1
            while j<k:
                s = A[i] + A[j] + A[k]
                diff = abs(s-B)
                if diff == 0:
                    return s
                if diff<mindiff:
                    mindiff = diff
                    result = s
                if s<=B:
                    j+=1
                else:
                    k-=1
        return result