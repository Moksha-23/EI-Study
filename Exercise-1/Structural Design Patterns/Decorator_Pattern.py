class Pizza:
    def get_description(self):
        return "Plain Pizza"

    def cost(self):
        return 10.00


class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def cost(self):
        return self.pizza.cost()


class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Cheese"

    def cost(self):
        return self.pizza.cost() + 1.50


class Olives(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Olives"

    def cost(self):
        return self.pizza.cost() + 1.00

my_pizza = Pizza()
my_pizza = Cheese(my_pizza)
my_pizza = Olives(my_pizza)

print(my_pizza.get_description())  
print(my_pizza.cost())  
