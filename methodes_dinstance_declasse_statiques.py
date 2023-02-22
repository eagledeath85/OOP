# -------------------- METHODES D'INSTANCE, DE CLASSE, ET STATIQUES --------------------

class Personne:
    # Variable de classe
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom

    # se_presenter() est une methode d'instance car on lui passe l'objet self
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.nom)} - {self.TYPE}")

    # formater_chaine() est une methode statique car on ne lui passe pas l'objet self
    # @staticmethod permet d'annoncer qu'il s'agit d'une methode statique
    @staticmethod
    def formater_chaine(chaine: str):
        return chaine.capitalize()

    # methode_de_classe() est une methode de classe car on lui passe le mot-cle cls
    @classmethod
    def methode_de_classe(cls):
        print(f"Methode de classe {cls}")


personne1 = Personne("jean")
personne1.se_presenter()

# Les methodes de classe peuvent etre appelees sans que l'on instancie d'objet au prealable
Personne.methode_de_classe()