def Inversion(n):
	if n < 10:
		return str(n)
	return str(n % 10) + Inversion(int(n /10))