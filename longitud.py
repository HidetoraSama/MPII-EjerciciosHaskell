def Longitud(n):
    if n < 10:
        return 1
    return 1 + Longitud(n / 10)