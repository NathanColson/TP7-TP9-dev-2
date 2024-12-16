from fraction import Fraction

# Création de fractions
f1 = Fraction(3, 4)  # 3/4
f2 = Fraction(5, 8)  # 5/8
f3 = Fraction(2, 3)  # 2/3
f4 = Fraction(6, -9)  # 6/-9 réduit en -2/3

print("Fraction 1 :", f1)
print("Fraction 2 :", f2)
print("Fraction 3 :", f3)
print("Fraction 4 (réduite) :", f4)

# Addition
result_add = f1 + f2
print(f"Addition ({f1} + {f2}) :", result_add)

# Soustraction
result_sub = f1 - f2
print(f"Soustraction ({f1} - {f2}) :", result_sub)

# Multiplication
result_mul = f1 * f2
print(f"Multiplication ({f1} * {f2}) :", result_mul)

# Division
result_div = f1 / f3
print(f"Division ({f1} / {f3}) :", result_div)

# Puissance
result_pow = f3 ** 2
print(f"Puissance ({f3} ** 2) :", result_pow)

# Comparaison
print(f"Comparaison : {f1} == {f2} ?", f1 == f2)
print(f"Comparaison : {f1} == {Fraction(6, 8)} ?", f1 == Fraction(6, 8))

# Décimal
print(f"Valeur décimale de {f1} :", float(f1))

# Propriétés
print(f"{f3} est zéro ?", f3.is_zero())
print(f"{f3} est entier ?", f3.is_integer())
print(f"{f3} est une fraction propre ?", f3.is_proper())
print(f"{f3} est une fraction unitaire ?", f3.is_unit())

# Nombre mixte
print(f"Nombre mixte de {Fraction(7, 3)} :", Fraction(7, 3).as_mixed_number())

# Fractions adjacentes
print(f"{f1} est adjacent à {Fraction(7, 4)} ?", f1.is_adjacent_to(Fraction(7, 4)))

# Cas d'erreurs
try:
    bad_fraction = Fraction(1, 0)  # Denominator cannot be 0
except ValueError as e:
    print("Erreur :", e)

try:
    bad_operation = f1 + "not a fraction"
except TypeError as e:
    print("Erreur :", e)
