import unittest
from fraction import Fraction


class FractionTestCase(unittest.TestCase):
    def test_init(self):
        """Verifying Fraction initialization and property getters"""
        self.assertEqual(Fraction(8, 5), Fraction(8, 5))
        self.assertEqual(Fraction(24, 9), Fraction(8, 3))
        self.assertRaises(TypeError, Fraction, 2, 3.5)
        self.assertRaises(TypeError, Fraction, 3.0, 6)
        self.assertRaises(TypeError, Fraction, "test", 4)
        self.assertRaises(TypeError, Fraction, 3, "value")
        self.assertEqual(Fraction(0, 7), Fraction(0, 1))
        self.assertRaises(ValueError, Fraction, 14, 0)
        self.assertEqual(Fraction(-9, 18), Fraction(-1, 2))
        self.assertEqual(Fraction(8, -3), Fraction(-8, 3))
        self.assertEqual(Fraction(-16, -8), Fraction(2, 1))

    def test_gcd(self):
        """Verifying gcd computing"""
        f = Fraction(1, 1)
        self.assertEqual(f.gcd(18, 6), 6)
        self.assertEqual(f.gcd(20, 16), 4)
        self.assertEqual(f.gcd(15, -10), 5)
        self.assertEqual(f.gcd(-12, -8), 4)

    def test_str(self):
        """Verifying the standard string format"""
        self.assertEqual(str(Fraction(10, 3)), "10/3")
        self.assertEqual(str(Fraction(5, 4)), "5/4")
        self.assertEqual(str(Fraction(20, 18)), "10/9")

    def test_as_mixed_number(self):
        """Verifying the mixed number string format"""
        self.assertEqual(Fraction(8, 3).as_mixed_number(), "2 and 2/3")
        self.assertEqual(Fraction(12, 4).as_mixed_number(), "3")

    def test_add(self):
        """Verifying the overloaded + operator"""
        self.assertEqual(Fraction(7, 3) + 6, Fraction(25, 3))
        self.assertRaises(TypeError, lambda: Fraction(4, 3) + 4.8)

    def test_sub(self):
        """Verifying the overloaded - operator"""
        self.assertEqual(Fraction(3, 4) - 3, Fraction(-9, 4))
        self.assertEqual(Fraction(8, 3) - 1, Fraction(5, 3))

    def test_mul(self):
        """Verifying the overloaded * operator"""
        self.assertEqual(Fraction(7, 5) * -4, Fraction(-28, 5))
        self.assertEqual(Fraction(8, 30) * -4, Fraction(-32, 30))
        self.assertRaises(TypeError, lambda: Fraction(7, 5) * 1.2)

    def test_truediv(self):
        """Verifying the overloaded / operator"""
        self.assertEqual(Fraction(5, 3) / Fraction(10, -4), Fraction(-2, 3))

    def test_pow(self):
        """Verifying the overloaded ** operator"""
        self.assertEqual(Fraction(6, 5) ** 2, Fraction(36, 25))
        self.assertEqual(Fraction(6, 5) ** Fraction(-2, 1), Fraction(25, 36))

    def test_eq(self):
        """Verifying the overloaded == operator"""
        self.assertFalse(Fraction(-9, 3) == Fraction(16, 32))
        self.assertTrue(Fraction(-9, 3) == -3)
        self.assertTrue(Fraction(16, 32) == Fraction(8, 16))
        self.assertFalse(Fraction(-9, 3) == Fraction(8, 16))

    def test_float(self):
        """Verifying the float format"""
        self.assertEqual(float(Fraction(4, 5)), 0.8)
        self.assertEqual(float(Fraction(100, 13)), 7.6923076923076925)
        self.assertEqual(float(Fraction(15, -42)), -0.35714285714285715)

    def test_is_zero(self):
        """Verifying the is_zero() method"""
        self.assertTrue(Fraction(0, 8).is_zero())
        self.assertFalse(Fraction(15, 10).is_zero())

    def test_is_integer(self):
        """Verifying the is_integer() method"""
        self.assertTrue(Fraction(10, 5).is_integer())
        self.assertFalse(Fraction(13, 6).is_integer())

    def test_is_proper(self):
        """Verifying the is_proper() method"""
        self.assertTrue(Fraction(4, 9).is_proper())
        self.assertFalse(Fraction(11, 2).is_proper())

    def test_is_unit(self):
        """Verifying the is_unit() method"""
        self.assertTrue(Fraction(1, 1).is_unit())
        self.assertFalse(Fraction(-1, 1).is_unit())

    def test_is_adjacent_to(self):
        """Verifying the is_adjacent_to() method"""
        self.assertTrue(Fraction(5, 2).is_adjacent_to(Fraction(7, 3)))


if __name__ == "__main__":
    unittest.main()
