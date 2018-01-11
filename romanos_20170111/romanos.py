valores = {
    'M':1000, 'D': 500, 'C':100,
    'L':50, 'X': 10, 'V': 5, 'I': 1
}

def romanos(n_romano):

    valor = 0
    for i, algarismo in enumerate(n_romano):
        multiplicador = 1
        atual = valores[algarismo]

        if i < len(n_romano)-1:
            prox_algarismo = n_romano[i+1]
            proximo = valores[prox_algarismo]
            if proximo > atual:
                multiplicador = -1
        
        valor += atual*multiplicador
    return valor