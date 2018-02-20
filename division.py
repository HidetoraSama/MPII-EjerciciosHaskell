def Division(n, m):
	if n < m:
		return 0
	return 1 + Division(n - m, m)