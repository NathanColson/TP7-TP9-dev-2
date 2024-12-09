from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """Build a fraction based on some numerator and denominator.

        PRE : Le dénominateur doit être non nul.
        POST : Les attributs `__num` et `__den` sont stockés sous leur forme la plus réduite.
        RAISES : ValueError si le dénominateur est nul, TypeError si les arguments ne sont pas des entiers.
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Les deux arguments doivent être des entiers.")
        if den == 0:
            raise ValueError("Le dénominateur d'une fraction ne peut pas être 0.")
        self.__num = num
        self.__den = den
        self.__reduce_form()

    def __reduce_form(self):
        """Réduit la fraction à sa forme la plus simple."""
        common_divisor = gcd(self.__num, self.__den)
        self.__num //= common_divisor
        self.__den //= common_divisor
        # Si le dénominateur est négatif, on ajuste les signes.
        if self.__den < 0:
            self.__num *= -1
            self.__den *= -1

    @property
    def numerator(self):
        """Retourne le numérateur de la fraction."""
        return self.__num

    @property
    def denominator(self):
        """Retourne le dénominateur de la fraction."""
        return self.__den

    def __str__(self):
        """
            Retourne une représentation textuelle de la fraction.

            Préconditions:
            - L'objet doit être une instance de la classe.
            - self.__num et self.__den doivent être des entiers représentant respectivement le numérateur et le dénominateur de la fraction.
            - self.__den ne doit pas être égal à zéro.

            Postconditions:
            - La fonction retourne une chaîne de caractères représentant la fraction sous la forme "numérateur/dénominateur" ou simplement "numérateur" si le dénominateur est 1.

            """
        if self.__den == 1:
            return f"{self.__num}"
        return f"{self.__num}/{self.__den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : Renvoie un entier et sa fraction restante
        """
        temp = ""
        if self.__num % self.__den != 0:
            # If there is a rest to the division
            temp = f" and {self.__num % self.__den}/{self.__den}"
        return f"{self.__num // self.__den}" + temp


    def __add__(self, other):
        """
            Ajoute une fraction ou un entier à la fraction courante.

            Pré:
            - L'objet doit être une instance de la classe Fraction.
            - L'argument 'other' doit être soit un entier, soit une autre instance de la classe Fraction.

            Post:
            - Si 'other' est un entier, la méthode retourne une nouvelle instance de Fraction avec l'entier converti en fraction (l'entier devient le numérateur, et le dénominateur est 1).
            - Si 'other' est une instance de Fraction, la méthode retourne une nouvelle instance de Fraction représentant la somme des deux fractions, avec un numérateur et un dénominateur réduits.

            Raise:
            - Lève une exception de type TypeError si 'other' n'est ni un entier ni une instance de Fraction.
            """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.__num * other.denominator + other.numerator * self.__den
            den = self.__den * other.denominator
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __sub__(self, other):
        """
            Soustrait une fraction ou un entier de la fraction courante.

            Préconditions:
            - L'objet doit être une instance de la classe Fraction.
            - L'argument 'other' doit être soit un entier, soit une autre instance de la classe Fraction.

            Postconditions:
            - Si 'other' est un entier, la méthode retourne une nouvelle instance de Fraction avec l'entier converti en fraction (l'entier devient le numérateur, et le dénominateur est 1).
            - Si 'other' est une instance de Fraction, la méthode retourne une nouvelle instance de Fraction représentant la différence des deux fractions, avec un numérateur et un dénominateur réduits.

            Raise:
            - Lève une exception de type TypeError si 'other' n'est ni un entier ni une instance de Fraction.
            """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.__num * other.denominator - other.numerator * self.__den
            den = self.__den * other.denominator
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __mul__(self, other):
        """
            Multiplie une fraction ou un entier avec la fraction courante.

            Préconditions:
            - L'objet doit être une instance de la classe Fraction.
            - L'argument 'other' doit être soit un entier, soit une autre instance de la classe Fraction.

            Postconditions:
            - Si 'other' est un entier, la méthode retourne une nouvelle instance de Fraction avec l'entier converti en fraction (l'entier devient le numérateur, et le dénominateur est 1).
            - Si 'other' est une instance de Fraction, la méthode retourne une nouvelle instance de Fraction représentant le produit des deux fractions, avec un numérateur et un dénominateur réduits.

            Raise:
            - Lève une exception de type TypeError si 'other' n'est ni un entier ni une instance de Fraction.
            """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.__num * other.numerator
            den = self.__den * other.denominator
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __truediv__(self, other):
        """
            Divise la fraction courante par une fraction ou un entier.

            Préconditions:
            - L'objet doit être une instance de la classe Fraction.
            - L'argument 'other' doit être soit un entier, soit une autre instance de la classe Fraction.

            Postconditions:
            - Si 'other' est un entier, la méthode retourne une nouvelle instance de Fraction avec l'entier converti en fraction (l'entier devient le numérateur, et le dénominateur est 1).
            - Si 'other' est une instance de Fraction, la méthode retourne une nouvelle instance de Fraction représentant le quotient des deux fractions, avec un numérateur et un dénominateur réduits.

            Raise:
            - Lève une exception de type ValueError si 'other' est une fraction avec un numérateur égal à 0 (division par zéro).
            - Lève une exception de type TypeError si 'other' n'est ni un entier ni une instance de Fraction.
            """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Pas de division par 0")
            num = self.__num * other.denominator
            den = self.__den * other.numerator
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions

        PRE : -
        POST : Renvoie un objet qui est la puissance other de notre object
        """
        new_num = self.__num ** other
        new_den = self.__den ** other
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        """
            Vérifie si la fraction courante est égale à une autre fraction ou un entier.

            Préconditions:
            - L'objet doit être une instance de la classe Fraction.
            - L'argument 'other' doit être soit un entier, soit une autre instance de la classe Fraction.

            Postconditions:
            - Retourne True si les fractions (ou la fraction et l'entier) sont égales, c'est-à-dire si leurs numérateurs et dénominateurs sont identiques.
            - Retourne False sinon.

            Raise:
            - Lève une exception de type TypeError si 'other' n'est ni un entier ni une instance de Fraction.
            """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return (self.__num == other.numerator) and (self.__den == other.denominator)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None
        POST : returns the decimal value of the fraction
        """
        return self.__num / self.__den

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None
        POST : returns True if the Fraction is equal to 0, False if not
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None
        POST : returns True if the Fraction represents an integer
        """
        return self.__den == 1  # Works because of the auto reduced form

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : Renvoie True si la Fraction est égale à une valeur strictement en dessous de 1
        """
        output = abs(self.__num) / abs(self.__den) < 1
        return output


    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None
        POST : returns True if the Fraction is equal to 1
        """
        return self.__num == self.__den

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference between them is a unit fraction

        PRE : None
        POST : returns True if the two values differ by a unit fraction, False if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return abs((self - other).__num) == 1
            # return (self._den == other._den) and (((self._num - 1) == other._num) or ((self._num + 1) == other._num))
        raise TypeError("You can only use Fraction's is_adjacent_to method with another Fraction or int")