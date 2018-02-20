def division(n, m):
	if n < m:
		return 0
	return 1 + division(n - m, m)