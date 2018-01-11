import unittest
from romanos import romanos

class RomanosTestCase(unittest.TestCase):
    def test_recebe_I_retorna_1(self):
        result = romanos('I')
        self.assertEqual(1, result)

    def test_recebe_V_retorna_5(self):
        result = romanos('V')
        self.assertEqual(5, result)

    def test_recebe_X_retorna_10(self):
        result = romanos('X')
        self.assertEqual(10, result)

    def test_recebe_L_retorna_50(self):
        result = romanos('L')
        self.assertEqual(50, result)

    def test_recebe_C_retorna_100(self):
        result = romanos('C')
        self.assertEqual(100, result)

    def test_recebe_D_retorna_500(self):
        result = romanos('D')
        self.assertEqual(500, result)

    def test_recebe_M_retorna_1000(self):
        result = romanos('M')
        self.assertEqual(1000, result)

    def test_recebe_II_retorna_2(self):
        result = romanos('II')
        self.assertEqual(2, result)

    def test_recebe_III_retorna_3(self):
        result = romanos('III')
        self.assertEqual(3, result)

    def test_recebe_XX_retorna_20(self):
        result = romanos('XX')
        self.assertEqual(20, result)

    def test_recebe_VI_retorna_6(self):
        result = romanos('VI')
        self.assertEqual(6, result)

    def test_recebe_VII_retorna_7(self):
        result = romanos('VII')
        self.assertEqual(7, result)

    def test_recebe_VIII_retorna_8(self):
        result = romanos('VIII')
        self.assertEqual(8, result)

    def test_recebe_IV_retorna_4(self):
        result = romanos('IV')
        self.assertEqual(4, result)

    def test_recebe_IX_retorna_9(self):
        result = romanos('IX')
        self.assertEqual(9, result)

    def test_recebe_IL_retorna_49(self):
        result = romanos('IL')
        self.assertEqual(49, result)

    def test_recebe_MDXC_retorna_1590(self):
        result = romanos('MDXC')
        self.assertEqual(1590, result)
    
    def test_recebe_MCMLXXXIV_retorna_1984(self):
        result = romanos('MCMLXXXIV')
        self.assertEqual(1984, result)

    def test_recebe_LII_retorna_52(self):
        result = romanos('LII')
        self.assertEqual(52, result)


unittest.main()