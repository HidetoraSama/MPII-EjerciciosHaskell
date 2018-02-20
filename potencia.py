def Potencia(m,n):

    if n==0:
        return 1
    if n==1:
        return m
    else:
        return m*Potencia(m,n-1)

print (Potencia(6,5))    
    
