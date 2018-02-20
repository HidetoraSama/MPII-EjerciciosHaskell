def MayorDigito(n):
    if n < 10:
        return n
    if (n % 10) > MayorDigito(int(n / 10)):
        return (n % 10)
    else:
        return MayorDigito(int(n / 10))