# --------------------- __str__ et __repr__ ---------------------

# Methode __str__
    # Permet de modifier la representation texte d'un objet
    # !!!!! Cette fonction retourne une chaine de caractere uniquement !!!!!
    # Representation sous forme d'une chaine de caracteres

# Methode __repr__
    # Permet de modifier la representation d'un objet
    # En lancant le programme en debug, l'objet sera representee par la valeur que retourne __repr__
    # Generalement des infos pour le developpeur pour la phase de dev

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_infos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    # def __str__(self):
    #     # return self.nom
    #     return str(self.__dict__)

    def __repr__(self):
        return f"{__class__.__name__} {str(self.__dict__)}"


personne1 = Personne("Robert", 49)
personne1.afficher_infos()

# Affiche la representation texte definit dans la methode __str__ ou la representation de l'objet definit dans __repr__
# La plus importante est __repr__
print(personne1)