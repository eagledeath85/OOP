class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = dict()     # dictionary that will store name, price, quantity for each item
        self.items_count = 0    # Count the number of items to add

    def add_item(self, name, price, quantity):
        if self.items_count + quantity > self.max_capacity:
            return False
        if name in self.items:
            return False

        self.items[name] = {'name': name, 'price': price, 'quantity': quantity}
        self.items_count += quantity
        return True

    def delete_item(self, name):
        if name not in self.items:
            return False
        self.items_count -= self.items[name]['quantity']
        del self.items[name]
        return True

    def get_most_stocked_item(self):
        most_stocked_item = None
        biggest_quantity = 0

        for item in self.items.values():
            name = item['name']
            quantity = item['quantity']

            if quantity > biggest_quantity:
                most_stocked_item = name
                biggest_quantity = quantity
        return most_stocked_item

    def get_items_in_price_range(self, min_price, max_price):
        items_list = []
        for item in self.items.values():
            name = item['name']
            price = item['price']
            if max_price >= price >= min_price:
                items_list.append(name)
        return items_list


i = Inventory(4)
i.add_item('Chocolate', 4.99, 1)
i.add_item('Cereal', 6.99, 1)
i.add_item('Milk', 3.99, 2)
i.add_item('Butter', 2.99, 1)
