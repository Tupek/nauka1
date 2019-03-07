class Product:
    id = 0
    name = None
    description = None
    price = 0.0
    quantity = 0
    __next_id = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        if price >= 0.01:
            self.price = float(price)
        else:
            raise ValueError("Incorrect price")
        if quantity > 0 and type(quantity) == int:
            self.quantity = quantity
        else:
            raise ValueError("Incorrect quantity")
        self.__id = self.__next_id
        Product.__next_id += 1

    def __id(self, id):
        return self.__id

    def get_total_sum(self):
        return self.quantity * self.price

    def get_id(self):
        return self.__id

    def __str__(self):
        return "{}, {}, {}, {}. {}".format(self.name, self.description, self.price, self.quantity, self.get_id())

p = Product("kawa", "mielona", 1, 5)
p2 = Product("ka4wa", "mielon4a", 18, 4)

