# --------------------- MODIFICATEURS D"ACCES ---------------------

# Modificateurs d'acces : public / private / protected

# public :
    # Acces depuis l'interieur et l'exterieur de la classe
# private :
    # Acces depuis l'interieur de la classe uniquement
    # Syntaxe : __nom_de_variable
# protected :
    # Acces depuis l'interieur de la classe et des classes derivees
    # Syntaze : _nom_de_variable


class Person:
    def __init__(self, nom, profession):
        self.__nom = nom    # variable private
        self._profession = profession   # variable protected

    def se_presenter(self):
        print(f"Je m'appelle {self.__nom}")


class Etudiant(Person):
    def se_presenter(self):
        super().se_presenter()
        print(f"Je suis {self._profession}")


personne1 = Etudiant("Jean", "etudiant")
personne1.se_presenter()