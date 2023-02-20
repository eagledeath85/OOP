# caracteristiques de la pizza : nom, prix, ingredients, vegetarienne (true/false)
# ces caracteristiques sont des variables d'instance

class Pizza:
    def __init__(self, name: str, price: float, ingredients: list, veggie: bool = False):
        self.name = name
        self.price = price # le prix des pizzas est un float
        self.ingredients = ingredients
        self.veggie = veggie

    def display(self):
        veg_str = ""
        if self.veggie:
            veg_str = " - VEGETARIENNE"
        print(f"PIZZA {self.name}: ${self.price}{veg_str}")
        print(", ".join(self.ingredients))
        print()

class CustomizablePizza(Pizza):
    BASIC_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    last_rank = 0
    def __init__(self):
        # On incremente de 1 la valeur de la variable de classe
        CustomizablePizza.last_rank += 1

        # la variable d'instance prend la valeur de la derniere variable de classe creee incrementee de un
        self.rank_of_pizza = CustomizablePizza.last_rank

        # On appelle le constructeur de la classe parent.
        # Celui ci prend les params name(str), price(float) et ingredients(list) en argument
        # On doit donc passer ces parametres dans notre appel
        super().__init__(f"Customizable {self.rank_of_pizza}", .0, [])
        self.ask_user_ingredients()
        self.calculate_customizable_pizza_price()


    def ask_user_ingredients(self):
        print("--------------")
        print(f"Ingredients pour la pizza personnalisee {self.rank_of_pizza}")
        while True:
            ingredients = input("Ajoutez un ingrédient ou appuyez sur ENTREE pour sortir : ")
            if ingredients == "":
                return
            self.ingredients.append(ingredients)
            print(f'Vous avez {len(self.ingredients)} ingrédient(s) : {", ".join(self.ingredients)}')

    def calculate_customizable_pizza_price(self):
        self.price =  self.BASIC_PRICE + (self.PRICE_PER_INGREDIENT * len(self.ingredients))


pizzas = [
            Pizza("4 fromages", 9.5, ["bleu", "emmental", "comte", "mozzarella"], True),
            Pizza("Regina", 10.5, ["jambon", "mozzarella", "champignons"]),
            Pizza("Norvegienne", 14.5, ["saumon", "emmental", "creme fraiche"]),
            Pizza("Marguarita", 8, ["mozzarella", "basilic", "tomate"], True),
            Pizza("Vegetarienne", 12.5, ["champignon", "poivrons", "olives", "tomate"], True),
            CustomizablePizza(),
            CustomizablePizza(),
        ]



def sorting_pizzas(element: Pizza) -> str:
    return element.name

# pizzas.sort(key=sorting_pizzas)

for pizza in pizzas:
        pizza.display()




