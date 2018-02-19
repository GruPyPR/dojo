import unittest
from caixa_eletronico import caixa_eletronico

class CaixaEletronicoTestCase(unittest.TestCase):

    def test_recebe_2_retorna_1_nota_de_2_reais(self):
        resultado = caixa_eletronico(2)
        self.assertEqual({2: 1}, resultado)

    def test_recebe_5_retorna_1_nota_de_5_reais(self):
        resultado = caixa_eletronico(5)
        self.assertEqual({5: 1}, resultado)

    def test_recebe_10_retorna_1_nota_de_10_reais(self):
        resultado = caixa_eletronico(10)
        self.assertEqual({10: 1}, resultado)

    def test_recebe_20_retorna_1_nota_de_20_reais(self):
        resultado = caixa_eletronico(20)
        self.assertEqual({20: 1}, resultado)

    def test_recebe_50_retorna_1_nota_de_50_reais(self):
        resultado = caixa_eletronico(50)
        self.assertEqual({50: 1}, resultado)

    def test_recebe_100_retorna_1_nota_de_100_reais(self):
        resultado = caixa_eletronico(100)
        self.assertEqual({100: 1}, resultado)

    def test_recebe_4_retorna_2_notas_de_2_reais(self):
        resultado = caixa_eletronico(4)
        self.assertEqual({2: 2}, resultado)

    def test_recebe_40_retorna_2_notas_de_20_reais(self):
        resultado = caixa_eletronico(40)
        self.assertEqual({20: 2}, resultado)

    def test_recebe_200_retorna_2_notas_de_100_reais(self):
        resultado = caixa_eletronico(200)
        self.assertEqual({100: 2}, resultado)

    def test_recebe_6_retorna_3_notas_de_2_reais(self):
        resultado = caixa_eletronico(6)
        self.assertEqual({2: 3}, resultado)

    def test_recebe_8_retorna_4_notas_de_2_reais(self):
        resultado = caixa_eletronico(8)
        self.assertEqual({2: 4}, resultado)

    def test_recebe_300_retorna_3_notas_de_100_reais(self):
        resultado = caixa_eletronico(300)
        self.assertEqual({100: 3}, resultado) 

    def test_recebe_400_retorna_4_notas_de_100_reais(self):
        resultado = caixa_eletronico(400)
        self.assertEqual({100: 4}, resultado) 

    def test_recebe_105_retorna_1_nota_de_100_reais_e_1_nota_de_5_reais(self):
        resultado = caixa_eletronico(105)
        self.assertEqual({100: 1,
                          5: 1}, resultado) 

    def test_recebe_110_retorna_1_nota_de_100_reais_e_1_nota_de_10_reais(self):
        resultado = caixa_eletronico(110)
        self.assertEqual({100: 1,
                          10: 1}, resultado)

    def test_recebe_15_retorna_1_nota_de_10_reais_e_1_nota_de_5_reais(self):
        resultado = caixa_eletronico(15)
        self.assertEqual({10: 1,
                          5: 1}, resultado)

    def test_recebe_250_retorna_2_notas_de_100_e_1_nota_de_50_reais(self):
        resultado = caixa_eletronico(250)
        self.assertEqual({100: 2, 50: 1}, resultado)
        
    def test_recebe_90_retorna_1_nota_de_50_e_2_nota_de_20_reais(self):
        resultado = caixa_eletronico(90)
        self.assertEqual({50: 1, 20: 2}, resultado)

    def test_recebe_370_retorna_3_nota_de_100_e_1_nota_de_50_reais_e_1_nota_20_reais(self):
        resultado = caixa_eletronico(370)
        self.assertEqual({100: 3, 50: 1, 20: 1}, resultado)

unittest.main()