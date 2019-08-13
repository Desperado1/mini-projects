"""DYNAMIC PROGRAMMING
a given array representing coin denominations and a non negative target amount
function returns ways to make change for that target amount.
"""

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	d = [0 for i in range(n + 1)]
	d[0] = 1
	for denom in denoms:
		for i in range(1, n + 1):
			if denom <= i:
				d[i] += d[i - denom]
	return d[-1]
