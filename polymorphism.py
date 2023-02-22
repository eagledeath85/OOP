# ------------------------ POLYMORPHISM ------------------------


# le polymorphisme est un concept qui fait référence à la capacité d’une variable, d’une fonction ou d’un objet
# à prendre plusieurs formes, c’est-à-dire à sa capacité de posséder plusieurs définitions différentes.


class Animaux:
    def __init__(self, nom):
        self.nom = nom

    def se_nourrir(self):
        # Instructions
        faim = True
        while faim:
            self.manger = True

    def se_deplacer(self):
        print("L'animal se deplace")

class Chien(Animaux):
    def __init__(self, nom):
        super().__init__(nom)

    def se_deplacer(self):
        super().se_deplacer()
        print(f"{self.nom} court")

class Aigle(Animaux):
    def __init__(self, nom):
        super().__init__(nom)

    def se_deplacer(self):
        super().se_deplacer()
        print("L'aigle vole")


class Dauphin(Animaux):
    def __init__(self, nom):
        super().__init__(nom)

    def se_deplacer(self):
        print("Le dauphin nage")


chien = Chien("Medor")
chien.se_deplacer()