def SumaDigitos(n):
    if n < 10:
        return n
    return (n % 10) + SumaDigitos(int(n / 10))