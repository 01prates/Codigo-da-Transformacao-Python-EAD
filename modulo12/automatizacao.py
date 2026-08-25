import unittest
from soma import soma


class TestSoma(unittest.TestCase):

    def test_soma_numeros_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_numeros_negativos(self):
        self.assertEqual(soma(-2, -3), -5)

    def test_soma_com_zero(self):
        self.assertEqual(soma(0, 5), 5)

    def test_soma_positivo_negativo(self):
        self.assertEqual(soma(10, -4), 6)

    def test_soma_float(self):
        self.assertAlmostEqual(soma(1.5, 2.5), 4.0)


if __name__ == "__main__":
    unittest.main()