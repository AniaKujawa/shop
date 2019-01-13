class Product:
    def __init__(self, name, price):
        self.name = name
        if type(price) is not int:
                raise Exception("You should type a number")
        else:
            self.price = price

    def __str__(self):
        return 'To jest ' + self.name + ' w cenie ' + str(self.price) + ' zl.'


class Client:
    def __init__(self, name, money):
        self.name = name
        if type(money) is not int:
                raise Exception("You should type a number")
        else:
            self.money = money

    def buy(self, product):
        if self.money >= product.price:
            self.money = self.money - product.price
            return True
        else:
            return False

    def __gt__(self, other):
        return self.money > other.money


class VIP(Client):

    def __init__(self, discount, name, money):
        super().__init__(name, money)
        if discount > 1 or discount < 0:
                raise Exception('Discount should be a value between 0 and 1')
        else:
            self.discount = discount

    def buy(self, product):
        if self.money >= (1 - self.discount) * product.price:
            self.money = self.money - (1 - self.discount) * product.price
            return True
        else:
            return False


class Shop:

    def __init__(self, products, name):
        self.products = products
        self.name = name

    def sell(self, client, product):
        try:
            product_on_list = any(elem.name == product.name and elem.price == product.price for elem in self.products)
            if not product_on_list:
                raise ValueError
        except ValueError:
            print("There is no such a product")
        else:
            return client.buy(product)



