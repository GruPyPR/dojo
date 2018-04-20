from magnetico import magnetico, Ponto


def assert_devolve_ponto_magnetico(ponto_magnetico, cursor):
    resultado = magnetico(ponto_magnetico, cursor)
    assert ponto_magnetico == resultado

def assert_devolve_cursor(ponto_magnetico, cursor):
    resultado = magnetico(ponto_magnetico, cursor)
    assert cursor == resultado


def test_magnetico_0_0_no_0_0():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(0, 0)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_0_no_6_0():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(6, 0)
    assert_devolve_cursor(ponto_magnetico, cursor)

def test_magnetico_0_0_no_0_6():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(0, 6)
    assert_devolve_cursor(ponto_magnetico, cursor)

def test_magnetico_0_0_no_0_3():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(0, 3)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_0_no_3_0():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(3, 0)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_0_no_4_0():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(4, 0)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_0_no_0_4():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(0, 4)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_0_no_5_0():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(5, 0)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_0_no_0_5():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(0, 5)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_0_no_5_5():
    ponto_magnetico = Ponto(0, 0)
    cursor = Ponto(5, 5)
    assert_devolve_cursor(ponto_magnetico, cursor)

def test_magnetico_1_0_no_6_0():
    ponto_magnetico = Ponto(1, 0)
    cursor = Ponto(6, 0)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_1_no_0_6():
    ponto_magnetico = Ponto(0, 1)
    cursor = Ponto(0, 6)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_0_1_no_0_7():
    ponto_magnetico = Ponto(0, 1)
    cursor = Ponto(0, 7)
    assert_devolve_cursor(ponto_magnetico, cursor)

def test_magnetico_1_0_no_7_0():
    ponto_magnetico = Ponto(1, 0)
    cursor = Ponto(7, 0)
    assert_devolve_cursor(ponto_magnetico, cursor)

def test_magnetico_1_1_no_1_7():
    ponto_magnetico = Ponto(1, 1)
    cursor = Ponto(1, 7)
    assert_devolve_cursor(ponto_magnetico, cursor)

def test_magnetico_1_2_no_1_7():
    ponto_magnetico = Ponto(1, 2)
    cursor = Ponto(1, 7)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_1_1_no_6_6():
    ponto_magnetico = Ponto(1,1)
    cursor = Ponto(6, 6)
    assert_devolve_cursor(ponto_magnetico, cursor)

def test_magnetico_1_1_no_1_6():
    ponto_magnetico = Ponto(1,1)
    cursor = Ponto(1, 6)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)

def test_magnetico_1_2_no_2_3():
    ponto_magnetico = Ponto(1, 2)
    cursor = Ponto(2, 3)
    assert_devolve_ponto_magnetico(ponto_magnetico, cursor)


def test_distancia_entre_