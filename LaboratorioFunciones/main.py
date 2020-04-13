def potencia(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado
print(4**3)
print(pow(4,3) )
print(potencia(4,3))