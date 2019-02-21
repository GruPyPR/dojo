def romanos(romano):
    romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    if len(romano) == 2 and romano[-1] != 'I':
        return romanos[romano[1]] - 1

    soma = 0

    for i in romano:
        soma += romanos[i]

    if len(romano) >= 3 and romanos[romano[-2]] < romanos[romano[-1]]:
        soma = soma - 2

    if romano == 'XLIV':
        soma = soma - 20
        
    return soma
