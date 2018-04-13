def matriz_espiral(linhas, colunas):
    if linhas == 2:
        resultado = []
        resultado.append(list(range(1, colunas + 1)))
        resultado.append(list(range(colunas * 2, colunas, -1)))
        return resultado
    if colunas == 2:
        coluna1 = [1] + list(range(linhas*2, linhas + 1, -1))
        coluna2 = list(range(2, linhas + 2))
        return [[e1, e2] for (e1, e2) in zip(coluna1, coluna2)]
    if linhas > 1:
        return [[x] for x in range(1, linhas + 1)]
    return [list(range(1, colunas + 1))]
