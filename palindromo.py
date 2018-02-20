def Palindromo(n):
	if len(n) <= 1:
		return True
	if n[0] == n[len(n) - 1]:
		return Palindromo(n[1:-1])
	else:
		return False