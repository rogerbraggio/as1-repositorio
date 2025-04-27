# tests/test_main.py

import unittest

class TestMain(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(2 + 3, 5)

    def test_subtracao(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplicacao(self):
        self.assertEqual(4 * 2, 8)

    def test_divisao(self):
        self.assertEqual(10 / 2, 5)

    def test_concatenacao_strings(self):
        self.assertEqual("Hello " + "World", "Hello World")

if __name__ == '__main__':
    unittest.main()
