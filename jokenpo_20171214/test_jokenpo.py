import unittest
from jokenpo import jokenpo, JogadaInvalidaError

class JokenpoTestCase(unittest.TestCase):
    def test_pedra_pedra_retorna_empate(self):
        resultado = jokenpo('pedra', 'pedra')
        self.assertEqual('EMPATE', resultado)

    def test_pedra_tesoura_retorna_pedra(self):
        resultado = jokenpo('pedra', 'tesoura')
        self.assertEqual('PEDRA', resultado)

    def test_pedra_papel_retorna_papel(self):
        resultado = jokenpo('pedra', 'papel')
        self.assertEqual('PAPEL', resultado)

    def test_tesoura_papel_retorna_tesoura(self):
        resultado = jokenpo('tesoura', 'papel')
        self.assertEqual('TESOURA', resultado)

    def test_tesoura_pedra_retorna_pedra(self):
        resultado = jokenpo('tesoura', 'pedra')
        self.assertEqual('PEDRA', resultado)

    def test_tesoura_tesoura_retorna_empate(self):
        resultado = jokenpo('tesoura', 'tesoura')
        self.assertEqual('EMPATE', resultado)

    def test_papel_papel_retorna_empate(self):
        resultado = jokenpo('papel', 'papel')
        self.assertEqual('EMPATE', resultado)

    def test_papel_pedra_retorna_papel(self):
        resultado = jokenpo('papel', 'pedra')
        self.assertEqual('PAPEL', resultado)

    def test_papel_tesoura_retorna_tesoura(self):
        resultado = jokenpo('papel', 'tesoura')
        self.assertEqual('TESOURA', resultado)

    def test_preda_preda_retorna_invalido(self):
        args = ('preda', 'preda')
        self.assertRaises(JogadaInvalidaError, jokenpo, *args)
        
    def test_tezoura_preda_retorna_invalido(self):
        args = ('tezoura', 'preda')
        self.assertRaises(JogadaInvalidaError, jokenpo, *args)

    def test_invalido_tesoura_retorna_invalido(self):
        args = ('preda', 'tesoura')
        self.assertRaises(JogadaInvalidaError, jokenpo, *args)

    def test_Papel_pedra_retorna_papel(self):
        resultado = jokenpo('Papel', 'pedra')
        self.assertEqual('PAPEL', resultado)

    def test_papel_Pedra_retorna_papel(self):
        resultado = jokenpo('papel', 'Pedra')
        self.assertEqual('PAPEL', resultado)

    def test_invalido_jogada1_inteiro(self):
        args = (1, 'pedra')
        self.assertRaises(JogadaInvalidaError, jokenpo, *args)
    
    def test_invalido_jogada2_inteiro(self):
        args = ('pedra', 1)
        self.assertRaises(JogadaInvalidaError, jokenpo, *args)
        
    def test_invalido_jogada1_none(self):
        args = (None, 'pedra')
        self.assertRaises(JogadaInvalidaError, jokenpo, *args)

    def test_invalido_jogada2_none(self):
        args = ('pedra', None)
        self.assertRaises(JogadaInvalidaError, jokenpo, *args)


unittest.main(verbosity=2)