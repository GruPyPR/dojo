import unittest
from lookandsay import lookandsay, separador 


# class LookAndSayTests(unittest.TestCase):
#     def teste_lookandsay_recebe_1_retorna_11(self):
#         result = lookandsay(1)
#         self.assertEqual(11, result)

#     def test_lookandsay_recebe_2_retorna_12(self):
#         result = lookandsay(2)
#         self.assertEqual(12, result)

#     def test_lookandsay_recebe_3_retorna_13(self):
#         result = lookandsay(3)
#         self.assertEqual(13, result)

#     def test_lookandsay_recebe_4_retorna_14(self):
#         result = lookandsay(4)
#         self.assertEqual(14, result)

#     def test_lookandsay_recebe_11_retorna_21(self):
#         result = lookandsay(11)
#         self.assertEqual(21, result)

#     def test_lookandsay_recebe_111_retorna_31(self):
#         result = lookandsay(111)
#         self.assertEqual(31, result)

#     def test_lookandsay_recebe_22_retorna_22(self):
#         result = lookandsay(22)
#         self.assertEqual(22, result)

#     def test_lookandsay_recebe_222_retorna_32(self):
#         result = lookandsay(222)
#         self.assertEqual(32, result)

#     def test_lookandsay_recebe_3333_retorna_43(self):
#         result = lookandsay(3333)
#         self.assertEqual(43, result)

#     def test_lookandsay_recebe_12_retorna_1112(self):
#         result = lookandsay(12)
#         self.assertEqual(1112,result)

#     def test_lookandsay_recebe_1121_retorna_211211(self):
#         result = lookandsay(1121)
#         self.assertEqual(211211,result)


class SeparadorTest(unittest.TestCase):
    def test_separador_recebe_ab_retorna_a_b(self):
        result = separador('ab')
        self.assertEqual(['a', 'b'], result)

    def test_separador_recebe_aa_retorna_aa(self):
        result = separador('aa')
        self.assertEqual(['aa'], result)
    
unittest.main()