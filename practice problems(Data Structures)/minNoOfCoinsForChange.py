def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	d = [float("inf") for i in range(n + 1)]
	d[0] = 0
	for denom in denoms:
		for i in range(1, n+1):
			if denom <= i:
				d[i] = min(d[i], d[i - denom] + 1)
	return d[n] if d[n] != float("inf") else -1
