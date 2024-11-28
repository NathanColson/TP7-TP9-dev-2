from math import gcd


class Fraction:
    """
    Class representing a fraction and operations on it.

    Author: V. Van den Schrieck
    Date: October 2021
    Updated: November 2024
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """
        Initialize a fraction with a numerator and a denominator.

        PRE: The denominator must not be zero.
        POST: Stores the fraction in reduced form (numerator and denominator
              divided by their greatest common divisor).
        EXCEPTIONS: Raises ZeroDivisionError if the denominator is 0.
        """
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être égal à 0.")

        commun = gcd(num, den)
        self._num = num // commun
        self._den = abs(den // commun)
        if den < 0:
            self._num = -self._num

    @property
    def numerator(self):
        """Returns the numerator of the fraction."""
        return self._num

    @property
    def denominator(self):
        """Returns the denominator of the fraction."""
        return self._den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """
        Return a string representation of the fraction.

        POST: Returns the numerator if the denominator is 1; otherwise,
              returns 'numerator/denominator'.
        """
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """
        Return the fraction as a mixed number (integer + proper fraction).

        POST: Returns the integer part if no remainder exists;
              otherwise, returns 'integer remainder/denominator'.
        """
        entier = self.numerator // self.denominator
        reste = abs(self.numerator % self.denominator)

        if reste == 0:
            return str(entier)
        return f"{entier} {reste}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """
        Overload the + operator to add two fractions.

        POST: Returns a new Fraction as the sum of the two fractions.
        EXCEPTIONS: Raises TypeError if 'other' is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une fraction.")
        num = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """
        Overload the - operator to subtract two fractions.

        POST: Returns a new Fraction as the difference between the two fractions.
        EXCEPTIONS: Raises TypeError if 'other' is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une fraction.")
        num = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        """
        Overload the * operator to multiply two fractions.

        POST: Returns a new Fraction as the product of the two fractions.
        EXCEPTIONS: Raises TypeError if 'other' is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une fraction.")
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        """
        Overload the / operator to divide two fractions.

        POST: Returns a new Fraction as the quotient of the two fractions.
        EXCEPTIONS: Raises TypeError if 'other' is not a Fraction.
                    Raises ZeroDivisionError if 'other.numerator' is 0.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une fraction.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division par une fraction avec un numérateur égal à 0.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __pow__(self, power):
        """Overloading of the ** operator for fractions

        PRE : faire un exposant avec une fraction
        POST : mets d'exposant à la fraction
        """
        num = self.numerator ** power
        den = self.denominator ** power
        return Fraction(num, den)

    def __eq__(self, other):
        """
        Overload the == operator to compare two fractions.

        POST: Returns True if the two fractions are equal; otherwise False.
        """
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """
        Return the decimal value of the fraction.

        POST: Returns the fraction's decimal equivalent.
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """
        Check if the fraction equals zero.

        POST: Returns True if the fraction is zero; otherwise False.
        """
        return self.numerator == 0

    def is_integer(self):
        """
        Check if the fraction is an integer.

        POST: Returns True if the fraction's numerator is a multiple of its denominator; otherwise False.
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """
        Check if the fraction is proper (absolute value < 1).

        POST: Returns True if proper; otherwise False.
        """
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """
        Check if the fraction is a unit fraction (numerator = 1).

        POST: Returns True if unit fraction; otherwise False.
        """
        return abs(self.numerator) == 1

    def is_adjacent_to(self, other):
        """
        Check if two fractions differ by a unit fraction.

        PRE: 'other' must be an instance of Fraction.
        POST: Returns True if adjacent; otherwise False.
        EXCEPTIONS: Raises TypeError if 'other' is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("L'opérande doit être une fraction.")
        diff_num = abs(self.numerator * other.denominator - self.denominator * other.numerator)
        diff_den = self.denominator * other.denominator
        return diff_num == 1


if __name__ == "__main__":
    # Example usage
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f1 + f2)
    print(f1.as_mixed_number())
