from mancala import mancala

def test_estado_inicial_1_0():
    estado = [
        [ 4, 4, 4, 4, 4, 4 ],
        [ 4, 4, 4, 4, 4, 4 ]
    ]
    resultado = mancala(estado, (1,0))
    esperado = [
        [4, 4, 4, 4, 4, 4],
        [0, 5, 5, 5, 5, 4]
    ]
    assert resultado == esperado

def test_estado_inicial_1_1():
    estado = [
        [ 4, 4, 4, 4, 4, 4 ],
        [ 4, 4, 4, 4, 4, 4 ]
    ]
    resultado = mancala(estado, (1,1))
    esperado = [
        [4, 4, 4, 4, 4, 4],
        [4, 0, 5, 5, 5, 5]
    ]
    assert resultado == esperado

def test_segundo_estado_1_0():
    estado = [
        [4, 4, 4, 4, 4, 4],
        [4, 0, 5, 5, 5, 5]
    ]
    resultado = mancala(estado, (1,0))
    esperado = [
        [4, 4, 4, 4, 4, 4],
        [0, 1, 6, 6, 6, 5]
    ]
    assert resultado == esperado


def test_estado_inicial_1_3():
    estado = [
        [4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4]
    ]
    resultado = mancala(estado, (1,3))
    esperado = [
        [4, 4, 4, 4, 5, 5],
        [4, 4, 4, 0, 5, 5]
    ]
    assert resultado == esperado

def test_segundo_estado_1_1():
    estado = [
        [4, 4, 4, 4, 4, 4],
        [0, 4, 5, 5, 5, 4]
    ]
    resultado = mancala(estado, (1,1))
    esperado = [
        [4, 4, 4, 4, 4, 4],
        [0, 0, 6, 6, 6, 5]
    ]
    assert resultado == esperado

def test_estado_inicial_1_2():
    estado = [
        [4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4]
    ]
    resultado = mancala(estado, (1,2))
    esperado = [
        [4, 4, 4, 4, 4, 5],
        [4, 4, 0, 5, 5, 5]
    ]
    assert resultado == esperado

def test_estado_radical_1_2():
    estado = [
        [0, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 4, 4]
    ]
    resultado = mancala(estado, (1,2))
    esperado = [
        [0, 0, 0, 0, 0, 1],
        [4, 4, 0, 5, 5, 5]
    ]
    assert resultado == esperado


def test_estado_radical_1_3():
    estado = [
        [0, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 4, 4]
    ]
    resultado = mancala(estado, (1, 3))
    esperado = [
        [0, 0, 0, 0, 1, 1],
        [4, 4, 4, 0, 5, 5]
    ]
    assert resultado == esperado

def test_estado_radical_1_4():
    estado = [
        [0, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 4, 4]
    ]
    resultado = mancala(estado, (1, 4))
    esperado = [
        [0, 0, 0, 0, 1, 1],
        [4, 4, 4, 0, 5, 5]
    ]
    assert resultado == esperado