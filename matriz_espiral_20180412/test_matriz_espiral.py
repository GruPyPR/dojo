from matriz_espiral import matriz_espiral

def test_matriz_de_1_por_1_retorna_1():
    linhas = 1
    colunas = 1
    esperado = [[1]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_1_por_2_retorna_1_2():
    linhas = 1
    colunas = 2
    esperado = [[1, 2]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_1_por_3_retorna_1_2_3():
    linhas = 1
    colunas = 3
    esperado = [[1, 2, 3]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_1_por_10_retorn_1_ate_10():
    linhas = 1
    colunas = 10
    esperado = [[1,2,3,4,5,6,7,8,9,10]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_2_por_1_retorna_1_2():
    linhas = 2
    colunas = 1
    esperado = [[1], [2]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_3_por_1_retorna_1_2_3():
    linhas = 3
    colunas = 1
    esperado = [[1], [2], [3]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_4_por_1_retorna_1_2_3_4():
    linhas = 4
    colunas = 1
    esperado = [[1], [2], [3], [4]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_10_por_1_retorna_1_ate_10():
    linhas = 10
    colunas = 1
    esperado = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_2_por_2_retorna_1_2__4_3():
    linhas = 2
    colunas = 2
    esperado = [[1, 2], [4, 3]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_2_por_3_retorna_1_2_3__6_5_4():
    linhas = 2
    colunas = 3
    esperado = [[1, 2, 3], [6, 5, 4]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_2_por_4_retorna_1_2_3_4__8_7_6_5():
    linhas = 2
    colunas = 4
    esperado = [[1, 2, 3, 4], [8, 7, 6, 5]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_2_por_5_retorna_1_2_3_4_5__10_9_8_7_6():
    linhas = 2
    colunas = 5
    esperado = [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_2_por_6_retorna_1_2_3_4_5_6__12_11_10_9_8_7():
    linhas = 2
    colunas = 6
    esperado = [[1, 2, 3, 4, 5, 6], [12, 11, 10, 9, 8, 7]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_2_por_10_retorna_1_ate_10__20_ate_11():
    linhas = 2
    colunas = 10
    esperado = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    ]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_4_por_2_retorna_espiral_4_2():
    linhas = 4
    colunas = 2
    esperado = [
        [1, 2],
        [8, 3],
        [7, 4],
        [6, 5]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_3_por_2_retorna_espiral_4_2():
    linhas = 3
    colunas = 2
    esperado = [
        [1, 2],
        [6, 3],
        [5, 4]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado


def test_matriz_de_5_por_2_retorna_espiral_4_2():
    linhas = 5
    colunas = 2
    esperado = [
        [ 1, 2],
        [10, 3],
        [ 9, 4],
        [ 8, 5],
        [ 7, 6]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_6_por_2_retorna_espiral_4_2():
    linhas = 6
    colunas = 2
    esperado = [
        [ 1, 2],
        [12, 3],
        [11, 4],
        [10, 5],
        [ 9, 6],
        [ 8, 7]]
    resultado = matriz_espiral(linhas, colunas)
    assert esperado == resultado

def test_matriz_de_3_por_3():
    lin