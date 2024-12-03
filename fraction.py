class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int=0, den: int=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : Aucun préalable.
        POST : Les attributs `numerator` et `denominator` sont stockés sous leur forme la plus réduite.
        L'utilisation des accesseurs garantit la gestion des erreurs.
        """
        self._num = None
        self._den = None
        self.numerator = num
        self.denominator = den

    @property
    def numerator(self):
        return self._num

    @property
    def denominator(self):
        return self._den

    @numerator.setter
    def numerator(self, num: int):
        """
        PRE : Aucun préalable.
        POST : Définit la variable interne `_num`. Réduit la fraction si possible.
        RAISES :  une exception si le type est incorrect.
        """
        if not isinstance(num, int):
            raise TypeError("Le numerator n'est pas un int")
        self._num = num
        if isinstance(self._den, int):
            self.reduce_form()

    @denominator.setter
    def denominator(self, den):
        """
        PRE : aucun préalable.
        POST : Définit la variable interne `_den`. Réduit la fraction si possible.
        RAISES : Si le type n'est pas correct. ValueError if den == 0
        """
        if not isinstance(den, int):
            raise TypeError("Le dénominateur d'une fraction doit être un entier")
        if not den:
            raise ValueError("Le dénominateur d'une fraction ne peut pas être 0")
        self._den = den
        if isinstance(self._num, int):
            self.reduce_form()

    def gcd(self, n: int, d: int):
        """
        Uses Euclid's algorithm to compute the GCD used to reduce the fraction form
        PRE : Les deux paramètres doivent être des entiers
        POST : Returns de GCD
        RAISES : TypeError if either argument is not an int
        """
        if not (isinstance(n, int) and isinstance(d, int)):
            raise TypeError("Les deux paramètres de la méthode gcd() doivent être des entiers")
        while d != 0:
            n, d = d, n % d
        return abs(n)

    def reduce_form(self):
        """
        Réduit la fraction à sa forme la plus simple.
         """
        d = self.gcd(self._num, self._den)
        self._num //= d
        self._den //= d
        if self._den < 0:
            self._num *= -1
            self._den *= -1

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : Aucun préalable.
        POST : Retourne une chaîne représentant la fraction sous forme réduite
        """
        den = ""
        if self._num % self._den:
            den = f"/{self._den}"
        return f"{self._num}" + den

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number
        A mixed number is the sum of an integer and a proper fraction

        PRE :  Aucun préalable.
        POST : Retourne une chaîne représentant la fraction comme une somme d'un entier et d'une fraction propre
        """
        rest = ""
        if self._num % self._den:
            rest = f" and {self._num % self._den}/{self._den}"
        return f"{self._num // self._den}" + rest

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne une nouvelle instance de Fraction représentant la somme de `self` et `other`.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
         """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = (self._num * other._den) + (other._num * self._den)
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("Votre Fraction n'est pas du bon type")

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne une nouvelle instance de Fraction représentant la différence entre `self` et `other`.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = (self._num * other._den) - (other._num * self._den)
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne une nouvelle instance de Fraction représentant le produit de `self` et `other`.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self._num * other._num
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction. `other` ne doit pas représenter 0.
        POST : Retourne une nouvelle instance de Fraction représentant le quotient de `self` et `other`.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction. ValueError si `other` représente 0.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            if not other._num:
                raise ValueError("Pas de division par 0")
            num = self._num * other._den
            den = self._den * other._num
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : `other` doit être un entier ou une Fraction représentant un entier.
        POST : Retourne une nouvelle instance de Fraction représentant `self` élevé à la puissance `other`.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction représentant un entier.
        """
        if isinstance(other, Fraction) and (not (other._num % other._den)):
            # other is a Fraction representing an integer
            other = int(other._num / other._den)
        if isinstance(other, int):
            if other >= 0:
                num = self._num ** other
                den = self._den ** other
            else:
                num = self._den ** -other
                den = self._num ** -other
            return Fraction(num, den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __eq__(self, other) :
        """Overloading of the == operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne True si `self` et `other` représentent la même valeur, sinon False.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return (self._num == other._num) and (self._den == other._den)
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __float__(self) :
        """Returns the decimal value of the fraction

         PRE : Aucun préalable.
        POST : Retourne la valeur décimale de la fraction.
        """
        return self._num / self._den

    def __ne__(self, other):
        """Overloading of the != operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne False si `self` et `other` représentent la même valeur, sinon True.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return not ((self._num == other._num) and (self._den == other._den))
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __gt__(self, other):
        """Overloading of the > operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne True si `self` représente une valeur supérieure à `other`, sinon False.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den > other._num * self._den
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __ge__(self, other):
        """Overloading of the >= operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne True si `self` est supérieur ou égal à `other`, sinon False.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den >= other._num * self._den
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __lt__(self, other):
        """Overloading of the < operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne True si `self` représente une valeur inférieure à `other`, sinon False.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den < other._num * self._den
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

    def __le__(self, other):
        """Overloading of the <= operator for fractions

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne True si `self` est inférieur ou égal à `other`, sinon False.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den <= other._num * self._den
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")

# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : Aucun préalable.
        POST : Retourne True si la valeur de la fraction est 0, sinon False.
        """
        return self._num == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Aucun préalable.
        POST : Retourne True si la fraction représente un entier.
        """
        return self._den == 1 # Works because of the auto reduced form

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : Aucun préalable.
        POST : Retourne True si la fraction représente une valeur absolue inférieure à 1
        """
        return float(self) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : Aucun préalable.
        POST : Retourne True si la fraction est égale à 1.
        """
        return self._num == self._den # == 1 because of the auto reduced form

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        PRE : `other` doit être un entier ou une instance de Fraction.
        POST : Retourne True si la différence absolue entre les deux fractions est une fraction unitaire, sinon False.
        RAISES : TypeError si `other` n'est pas un entier ou une Fraction.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return abs((self - other)._num) == 1
        raise TypeError("Vous ne pouvez utiliser cette méthode seulement avec un entier ou une Fraction")