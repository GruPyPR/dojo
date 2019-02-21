import pytest
from romanos import romanos

def test_I_retorna_1():
    assert romanos('I') == 1

def test_V_retorna_5():
    assert romanos('V') == 5

def test_X_retorna_10():
    assert romanos('X') == 10

def test_L_retorna_50():
    assert romanos('L') == 50

def test_C_retorna_100():
    assert romanos('C') == 100

def test_D_retorna_500():
    assert romanos('D') == 500

def test_M_retorna_1000():
    assert romanos('M') == 1000

def test_II_retorna_2():
    assert romanos('II') == 2

def test_III_retorna_3():
    assert romanos('III') == 3

def test_IV_retorna_4():
    assert romanos('IV') == 4

def test_VI_retorna_6():
    assert romanos("VI") == 6

def test_IX_retorna_9():
    assert romanos("IX") == 9

def test_XI_retorna_11():
    assert romanos("XI") == 11

def test_XIV_retorna_14():
    assert romanos("XIV") == 14

def test_XXIV_retorna_24():
    assert romanos("XXIV") == 24

def test_XXXIV_retorna_34():
    assert romanos("XXXIV") == 34

def test_LIV_retorna_54():
    assert romanos("LIV") == 54

def test_XXXIX_retorna_39():
    assert romanos("XXXIX") == 39

def test_XLIV_retorna_44():
    assert romanos('XLIV') == 44

def test_XLIX_retorna_49():
    assert romanos('XLIX') == 49

def test_w_retorna_exception():
    with pytest.raises(KeyError):
        romanos('W')
