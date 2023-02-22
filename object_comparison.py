# --------------------- COMPARER DES OBJETS ---------------------
# is / ==

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_infos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    # On peut implementer une fonction qui redefinit l'egalite voulue
    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age

personne1 = Personne("Robert", 49)
personne1.afficher_infos()

personne2 = Personne("Claire", 27)
personne2.afficher_infos()

# Comparer personne1 et personne2 avec is retournera False car ce sont 2 objets distincts
print(personne1 is personne2)

# Cette comparaison pourra retourner True si la fonction __eq__ a ete redefini
print(personne1 == personne2)

# Si l'on n'a pas acces au code, on peut toujours comparer les dictionnaires resultants des objets grace a __dict__
print(personne1.__dict__ == personne2.__dict__)
print(personne1.__dict__)