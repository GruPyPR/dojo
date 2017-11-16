import unittest

from fizzbuzz import fizzbuzz, FizzBuzzInt

class FizzBuzzTestCase(unittest.TestCase):

    def test_fizzbuzz_1_retorna_1(self):
        result = fizzbuzz(1)
        self.assertEqual(1, result)

    def test_fizzbuzz_2_retorna_2(self):
        result = fizzbuzz(2)
        self.assertEqual(2, result)
    
    def test_fizzbuzz_3_retorna_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual('fizz', result)

    def test_fizzbuzz_4_retorna_4(self):
        result = fizzbuzz(4)
        self.assertEqual(4, result)

    def test_fizzbuzz_5_retorna_buzz(self):
        result = fizzbuzz(5)
        self.assertEqual('buzz', result)

    def test_fizzbuzz_6_retorna_fizz(self):
        result = fizzbuzz(6)
        self.assertEqual('fizz', result)
 
    def test_fizzbuzz_7_retorna_7(self):
        result = fizzbuzz(7)
        self.assertEqual(7, result)

    def test_fizzbuzz_9_retorna_fizz(self):
        result = fizzbuzz(9)
        self.assertEqual('fizz', result)

    def test_fizzbuzz_10_retorna_buzz(self):
        result = fizzbuzz(10)
        self.assertEqual('buzz', result)

    def test_fizzbuzz_15_retorna_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual('fizzbuzz', result)

    def test_int_fizz_buzz_1_retorna_1(self):
        fizzbuzz_int = FizzBuzzInt(1)
        self.assertEqual(fizzbuzz_int.to_fizzbuzz(), 1)

    def test_int_fizz_buzz_2_retorna_2(self):
        fizzbuzz_int = FizzBuzzInt(2)
        self.assertEqual(fizzbuzz_int.to_fizzbuzz(), 2)

    def test_int_fizz_buzz_3_retorna_3(self):
        fizzbuzz_int = FizzBuzzInt(3)
        self.assertEqual(fizzbuzz_int.to_fizzbuzz(), 'fizz')

    def test_repr_fizz_buzz_int_3(self):
        fizzbuzz_int = FizzBuzzInt(3)
        self.assertEqual(repr(fizzbuzz_int), repr('fizz'))

    def test_repr_fizz_buzz_int_5(self):
        fizzbuzz_int = FizzBuzzInt(5)
        self.assertEqual(repr(fizzbuzz_int), repr('buzz'))

    def test_repr_fizz_buzz_int_13(self):
        fizzbuzz_int = FizzBuzzInt(13)
        self.assertEqual(repr(fizzbuzz_int), repr(13))


unittest.main()