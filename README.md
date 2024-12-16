# TP7-TP9-dev-2
# Gestion des Exceptions en Python

Les exceptions en Python permettent de gérer les erreurs qui peuvent survenir pendant l'exécution d'un programme. Bien gérer les exceptions est crucial pour éviter que le programme ne se termine brutalement et pour informer l'utilisateur ou le développeur de manière claire sur ce qui a causé l'erreur.

## **1. Qu'est-ce qu'une exception ?**
Une exception est un événement qui interrompt le flux normal du programme lorsqu'une erreur survient. Python fournit plusieurs types d'exceptions prédéfinies, comme :

- `ValueError`: Quand une valeur n'est pas correcte.
- `TypeError`: Quand un type de données est incorrect.
- `ZeroDivisionError`: Quand on tente de diviser un nombre par zéro.
- `FileNotFoundError`: Quand un fichier demandé n'est pas trouvé.

### Exemple de base :
```python
x = int("abc")  # Cette ligne générera une exception de type ValueError
```

---

## **2. Différences entre `raise` et `try/except`**

### **`raise` : Lancer une exception**
- Le mot-clé `raise` est utilisé pour signaler une exception.
- On l'utilise souvent dans une fonction ou une classe pour indiquer qu'une condition anormale a été rencontrée.

#### Syntaxe :
```python
raise NomDeLException("Message d'erreur")
```

#### Exemple :
```python
def diviser(a, b):
    if b == 0:
        raise ValueError("Le dénominateur ne peut pas être 0.")
    return a / b

# Appel de la fonction
resultat = diviser(10, 0)  # Lèvera une exception ValueError
```

Dans cet exemple, si `b` vaut 0, l'exception est levée ("raise") avec un message explicite.

### **`try/except` : Gérer une exception**
- La structure `try/except` est utilisée pour capturer une exception et la gérer de manière contrôlée.
- Cela permet d'éviter qu'une erreur stoppe brutalement le programme.

#### Syntaxe :
```python
try:
    # Code susceptible de générer une exception
    instruction_risqueuse()
except NomDeLException as e:
    # Code pour gérer l'exception
    print(f"Erreur : {e}")
```

#### Exemple :
```python
try:
    resultat = diviser(10, 0)
except ValueError as e:
    print("Une erreur est survenue :", e)
```

Dans cet exemple, l'exception `ValueError` est interceptée, et un message est affiché sans que le programme ne plante.

---

## **3. Quand utiliser `raise` et `try/except` ?**

### **Cas d'utilisation de `raise` :**
- Lorsqu'on écrit une fonction ou une classe et qu'on souhaite **signaler une erreur à l'utilisateur**.
- Exemple :
  ```python
  def verifier_age(age):
      if age < 0:
          raise ValueError("L'âge ne peut pas être négatif.")
  ```

### **Cas d'utilisation de `try/except` :**
- Lorsqu'on appelle une fonction ou un bloc de code potentiellement risqué et qu'on veut **gérer proprement l'erreur**.
- Exemple :
  ```python
  try:
      verifier_age(-5)
  except ValueError as e:
      print("Erreur capturée :", e)
  ```

---

## **4. La clause `finally` : Toujours exécuter un bloc de code**

La clause `finally` est utilisée pour exécuter du code qui doit l'être peu importe si une exception a été levée ou non. Par exemple, fermer un fichier ou libérer une ressource.

#### Exemple :
```python
try:
    fichier = open("mon_fichier.txt", "r")
    contenu = fichier.read()
except FileNotFoundError:
    print("Fichier introuvable.")
finally:
    print("Bloc finally : toujours exécuté.")
    fichier.close()
```

---

## **5. Bonnes pratiques avec les exceptions**
- **Ne gérez que les exceptions que vous comprenez :** Évitez d'utiliser un bloc `except` vide ou général.
  ```python
  try:
      resultat = diviser(10, 0)
  except Exception:  # Mauvaise pratique
      pass
  ```
- **Soyez précis dans vos exceptions :** Ciblez des types d'exceptions précis.
  ```python
  except ValueError:
      print("Valeur incorrecte.")
  ```
- **Ajoutez des messages explicites :** Lors de l'utilisation de `raise`, fournissez un message clair.
  ```python
  raise ValueError("Le numérateur et le dénominateur doivent être des entiers.")
  ```
- **Utilisez `finally` pour nettoyer :** Libérez toujours les ressources comme les fichiers ou connexions.

---

## **6. Exemples concrets dans le fichier `Fraction`**
Dans votre classe `Fraction`, vous utilisez `raise` pour signaler des erreurs comme des types incorrects ou un dénominateur nul. Voici un exemple de gestion dans un fichier utilisateur :

```python
from fraction import Fraction

try:
    f = Fraction(1, 0)  # Cette ligne lève une ValueError
except ValueError as e:
    print("Erreur capturée :", e)
```

Ce type de structure permet à l'utilisateur de votre classe de gérer proprement les erreurs sans arrêter le programme.

