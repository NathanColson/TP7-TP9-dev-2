import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    """Tests unitaires pour la classe Fraction"""

    def test_initialization(self):
        """Test de l'initialisation et de la réduction automatique des fractions"""
        f = Fraction(6, 8)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)  # Test de l'exception pour un dénominateur de 0

    def test_str_and_mixed_number(self):
        """Test des représentations textuelles (__str__ et as_mixed_number)"""
        f = Fraction(7, 4)
        self.assertEqual(str(f), "7/4")
        self.assertEqual(f.as_mixed_number(), "1 3/4")

        f2 = Fraction(4, 2)
        self.assertEqual(str(f2), "2")  # Test pour un entier
        self.assertEqual(f2.as_mixed_number(), "2")

    def test_addition(self):
        """Test de l'opérateur +"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result, Fraction(5, 6))

    def test_subtraction(self):
        """Test de l'opérateur -"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        result = f1 - f2
        self.assertEqual(result, Fraction(1, 4))

    def test_multiplication(self):
        """Test de l'opérateur *"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        self.assertEqual(result, Fraction(1, 2))

    def test_division(self):
        """Test de l'opérateur /"""
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 5)
        result = f1 / f2
        self.assertEqual(result, Fraction(15, 8))

        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)  # Test de la division par une fraction nulle

    def test_equality(self):
        """Test de l'opérateur =="""
        f1 = Fraction(2, 3)
        f2 = Fraction(4, 6)
        self.assertTrue(f1 == f2)  # Les deux fractions sont égales

        f3 = Fraction(1, 2)
        self.assertFalse(f1 == f3)

    def test_properties(self):
        """Test des méthodes is_zero, is_integer, is_proper, is_unit"""
        f1 = Fraction(0, 5)
        self.assertTrue(f1.is_zero())

        f2 = Fraction(6, 3)
        self.assertTrue(f2.is_integer())
        self.assertFalse(f2.is_proper())

        f3 = Fraction(1, 4)
        self.assertTrue(f3.is_proper())
        self.assertTrue(f3.is_unit())

    def test_is_adjacent_to(self):
        """Test de la méthode is_adjacent_to"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertTrue(f1.is_adjacent_to(f2))

        f3 = Fraction(3, 4)
        self.assertFalse(f1.is_adjacent_to(f3))

    def test_exponentiation(self):
        """Test de l'opérateur **"""
        f = Fraction(2, 3)
        result = f ** 2
        self.assertEqual(result, Fraction(4, 9))

"""
**Lancer les tests**

Pour exécuter les tests, utilisez la commande suivante dans le terminal ou un IDE compatible :
```bash
python -m unittest test_fraction.py
"""