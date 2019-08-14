"""DYNAMIC PROGRAMMING
minimum no of operations required on string1 to make it like string2
"""

def levenshteinDistance(str1, str2):
    # Write your code here.
	d = [[i for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		d[i][0] = d[i-1][0] + 1
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				d[i][j] = d[i-1][j-1]
			else:
				d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])
	return d[-1][-1]
