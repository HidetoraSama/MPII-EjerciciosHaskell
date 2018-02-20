def Producto(m,n):
    if m == 0:
        return 0
    if m == 1:
        return n
    else:
        return n + Producto(n, m - 1)