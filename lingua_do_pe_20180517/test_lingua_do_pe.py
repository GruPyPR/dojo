import pytest

from lingua_do_pe import P


def test_x_retorna_xpx():
    resultado = P('x')
    assert resultado == 'xpx'

@pytest.mark.parametrize(
    'entrada,esperado', 
    (
        ('a', 'apa'), ('e','epe'),
        ('i', 'ipi'), ('o', 'opo'),
        ('u', 'upu'),
    )
)
def test_vogal_retorna_vogalpvogal(entrada, esperado):
    resultado = P(entrada)
    assert resultado == esperado

def test_go_retorna_gopo():
    resultado = P('go')
    assert resultado == 'gopo'

def test_na_retorna_napa():
    resultado = P('na')
    assert resultado == 'napa'

def test_da_retorno_dapa():
    resultado = P('da')
    assert resultado == 'dapa'

def test_c_return_cpc():
    resultado = P('c')
    assert resultado == 'cpc'

def test_au_return_apaupu():
    resultado = P('au')
    assert resultado == 'apaupu'

def test_ai_return_apaipi():
    resultado = P('ai')
    assert resultado == 'apaipi'

def test_bola_return_bopolapa():
    resultado = P('bola')
    assert resultado == 'bopolapa'

def test_rato_return_rapatopo():
    resultado = P('rato')
    assert resultado == 'rapatopo'

def test_palavra_return_papalapavpvrapa():
    resultado = P('palavra')
    assert resultado == 'papalapavpvrapa'
