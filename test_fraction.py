import unittest
from fraction import Fraction


class FractionTestCase(unittest.TestCase):
    def test_init(self):
        frac1 = Fraction(34, 58)
        self.assertEqual(frac1.numerator, 17)
        self.assertEqual(frac1.denominator, 29)

        frac2 = Fraction()
        self.assertEqual(frac2.numerator, 0)
        self.assertEqual(frac2.denominator, 1)

        frac3 = Fraction(-27, -29)
        self.assertEqual(frac3.numerator, 27)
        self.assertEqual(frac3.denominator, 29)

        frac4 = Fraction(13, -21)
        self.assertEqual(frac4.numerator, -13)
        self.assertEqual(frac4.denominator, 21)

        with self.assertRaises(ValueError):
            Fraction(3, 0)

    def test_string(self):
        frac1 = Fraction(34, 58)
        self.assertEqual(frac1.__str__(), "17/29")

        frac2 = Fraction(1, 4)
        self.assertEqual(frac2.__str__(), "1/4")

        frac3 = Fraction(-1, 2)
        self.assertEqual(frac3.__str__(), "-1/2")

        frac4 = Fraction(4, 4)
        self.assertEqual(frac4.__str__(), "1")

        frac5 = Fraction(1, -5)
        self.assertEqual(frac5.__str__(), "-1/5")

        frac6 = Fraction(-1, -2)
        self.assertEqual(frac6.__str__(), "1/2")

        frac7 = Fraction(0, 10)
        self.assertEqual(frac7.__str__(), "0")

    def test_as_mixed_number(self):
        frac1 = Fraction(7, 3)
        self.assertEqual(frac1.as_mixed_number(), "2 and 1/3")

        frac2 = Fraction(6, 3)
        self.assertEqual(frac2.as_mixed_number(), "2")

        frac3 = Fraction(1, 3)
        self.assertEqual(frac3.as_mixed_number(), "0 and 1/3")

        frac4 = Fraction(-7, 3)
        self.assertEqual(frac4.as_mixed_number(), "-3 and 2/3")

        frac5 = Fraction(-9, 3)
        self.assertEqual(frac5.as_mixed_number(), "-3")

        frac6 = Fraction(0, 3)
        self.assertEqual(frac6.as_mixed_number(), "0")

    def test_add(self):
        # Test addition de fractions avec le même dénominateur
        frac1 = Fraction(3, 5)
        frac2 = Fraction(2, 5)
        result = frac1 + frac2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

        # Test addition avec zéro
        frac3 = Fraction(3, 4)
        frac4 = Fraction(0, 3)
        result2 = frac3 + frac4
        self.assertEqual(result2.numerator, 3)
        self.assertEqual(result2.denominator, 4)

        # Test addition avec des fractions ayant des signes différents
        frac5 = Fraction(-1, 2)
        frac6 = Fraction(1, 4)
        result3 = frac5 + frac6
        self.assertEqual(result3.numerator, -1)
        self.assertEqual(result3.denominator, 4)

        # Test addition avec des types invalides
        with self.assertRaises(TypeError):
            frac1 + "4"  # Une chaîne de caractères, pas un entier ou une Fraction

    def test_mul(self):
        frac1 = Fraction(3, 4)
        frac2 = Fraction(0, 5)
        frac3 = Fraction(2, 5)
        frac4 = Fraction(-2, 5)

        # Test division par une fraction nulle
        with self.assertRaises(ValueError):
            frac1 / frac2  # Division par zéro (numérateur de `frac2` est 0)

        # Test division par un type invalide
        with self.assertRaises(TypeError):
            frac1 / "2"  # Une chaîne de caractères, pas un entier ou une fraction

        # Cas valides
        result1 = frac1 / frac3
        self.assertEqual(result1.numerator, 15)
        self.assertEqual(result1.denominator, 8)

        result2 = frac1 / frac4
        self.assertEqual(result2.numerator, -15)
        self.assertEqual(result2.denominator, 8)

        with self.assertRaises(ValueError):
            frac1 / frac2  # `frac2` a un numérateur de 0

    def test_truediv(self):
        """"Verifying the overloaded / operator"""
        f1, f2, f3 = Fraction(9, 5), Fraction(8, -2), 5
        self.assertEqual(f1 / f2, Fraction(-9, 20))
        self.assertEqual(f2 / f1, Fraction(-20, 9))
        self.assertEqual(f1 / f3, Fraction(9, 25))
        self.assertEqual(f2 / f3, Fraction(-4, 5))
        with self.assertRaises(ValueError):
            f1 / 0
        with self.assertRaises(TypeError):
            f1 / 2.1

    def test_pow(self):
        # Cas positif: puissance positive
        frac1 = Fraction(2, 3)
        result = frac1 ** 2
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 9)

        # Cas négatif: puissance positive
        frac2 = Fraction(-2, 3)
        result = frac2 ** 3
        self.assertEqual(result.numerator, -8)
        self.assertEqual(result.denominator, 27)

        # Cas puissance 0: tout nombre à la puissance 0 donne 1
        frac3 = Fraction(2, 5)
        result = frac3 ** 0
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

        # Cas spécial: fraction avec numérateur 0
        frac5 = Fraction(0, 5)
        result = frac5 ** 3
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

        # Cas spécial: puissance négative sur fraction nulle (doit lever une exception)
        with self.assertRaises(ZeroDivisionError):
            frac5 ** -1  # Fraction 0 ne peut pas être inversée

        # Cas avec exposant 1: doit renvoyer la même fraction
        frac6 = Fraction(7, 8)
        result = frac6 ** 1
        self.assertEqual(result.numerator, 7)
        self.assertEqual(result.denominator, 8)

        # Cas avec fraction négative et puissance paire
        frac7 = Fraction(-3, 4)
        result = frac7 ** 2
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 16)

    def test_eq(self):
        frac1 = Fraction(2, 3)
        frac2 = Fraction(2, 3)
        self.assertTrue(frac1 == frac2)

        frac3 = Fraction(3, 4)
        self.assertFalse(frac1 == frac3)

        frac5 = Fraction(0, 5)
        frac6 = Fraction(0, 10)
        self.assertTrue(frac5 == frac6)

        frac7 = Fraction(-2, 3)
        self.assertFalse(frac1 == frac7)

        # Test comparaison avec un type invalide
        with self.assertRaises(TypeError):
            frac1 == "4"  # Comparer avec une chaîne de caractères

        with self.assertRaises(TypeError):
            frac1 == 2.5  # Comparer avec un float

    def test_float(self):
        """"Verifying the float format"""
        f1, f2, f3, f4 = Fraction(5, 6), Fraction(93, 14), Fraction(9, -32), Fraction(-12, -35)
        self.assertEqual(float(f1), 0.8333333333333334)
        self.assertEqual(float(f2), 6.642857142857143)
        self.assertEqual(float(f3), -0.28125)
        self.assertEqual(float(f4), 0.34285714285714286)

    def test_is_zero(self):
        """Verifying the is_zero() method"""
        f1, f2, f3 = Fraction(0, 7), Fraction(12, 9), Fraction(0, -5)
        self.assertTrue(f1.is_zero())
        self.assertFalse(f2.is_zero())
        self.assertTrue(f3.is_zero())


    def test_is_integer(self):
        frac1 = Fraction(8, 4)
        self.assertTrue(frac1.is_integer())

        frac2 = Fraction(3, 1)
        self.assertTrue(frac2.is_integer())

        frac3 = Fraction(5, 3)
        self.assertFalse(frac3.is_integer())

        frac4 = Fraction(-8, 4)
        self.assertTrue(frac4.is_integer())

    def test_is_unit(self):
        """Verifying the is_unit() method"""
        f1, f2, f3 = Fraction(1, 3), Fraction(1, 1), Fraction(-1, 1)
        self.assertFalse(f1.is_unit())
        self.assertTrue(f2.is_unit())
        self.assertFalse(f3.is_unit())

    def test_is_proper(self):
        frac1 = Fraction(1, 2)
        self.assertTrue(frac1.is_proper())

        frac2 = Fraction(-2, 5)
        self.assertTrue(frac2.is_proper())

        frac3 = Fraction(5, 3)
        self.assertFalse(frac3.is_proper())

        frac4 = Fraction(1, 1)
        self.assertFalse(frac4.is_proper())

        frac5 = Fraction(-2, 2)
        self.assertFalse(frac5.is_proper())

        frac_zero = Fraction(0, 10)
        self.assertTrue(frac_zero.is_proper())

    def test_is_adjacent(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 2)
        self.assertTrue(frac1.is_adjacent_to(frac2))

        frac3 = Fraction(-1, 3)
        frac4 = Fraction(5, 6)
        self.assertFalse(frac3.is_adjacent_to(frac4))

        frac1 = Fraction(1, 2)  # 1/2
        with self.assertRaises(TypeError):
            frac1.is_adjacent_to("Not a fraction")


if __name__ == "__main__":
    unittest.main()
