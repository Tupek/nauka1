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
        if self.quantity >= 3:
            return self.quantity * self.price * 0.8
        else:
            return self.quantity * self.price

    def get_id(self):
        return self.__id

class ShopingCart:
    products = {}

    def add_product(self, new_product):
        self.products[new_product.get_id] = new_product

    def remove_product_quantity(self, product_id):
        self.product_id = product_id
        if self.product_id in self.products:
            del self.products[product_id]
        else:
            pass

    def change_product_quantity(self, product_id, new_quantity):
        self.product_id = product_id
        self.new_quantity = new_quantity
        if self.product_id in self.products:
            self.products[product_id].quantity = self.new_quantity
        else:
            pass

    def print_receipt(self):
        total = 0
        for id in self.products:
            print(self.products[id].name, '-', self.products[id].price, self.products[id].quantity, self.products[id].get_total_sum())
            total += self.products[id].get_total_sum()
        print(total)


p = Product("kawa", "mielona", 18, 5)
p2 = Product("kielbasa", "slaska - szt.", 2, 2)

s = ShopingCart()
s.add_product(p)
s.add_product(p2)
s.change_product_quantity(p.get_id, 11)
#s.remove_product_quantity(p2.get_id)
s.print_receipt()