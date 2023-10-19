# Component  arayüzü
class Tea:
    def cost(self):
        return 5

# Concrete Component  -  Çay
class SimpleTea(Tea):
    def cost(self):
        return 5

# Concrete Decorator  - Şeker
class SugarDecorator(Tea):
    def __init__(self, decorated_tea):
        self.decorated_tea = decorated_tea

    def cost(self):
        return self.decorated_tea.cost() + 1

# Concrete Decorator  - Süt
class MilkDecorator(Tea):
    def __init__(self, decorated_tea):
        self.decorated_tea = decorated_tea

    def cost(self):
        return self.decorated_tea.cost() + 2

if __name__ == "__main__":
    simple_tea = SimpleTea()
    print("Basit Çay Fiyatı:", simple_tea.cost())

    tea_with_sugar = SugarDecorator(simple_tea)
    print("Şeker Eklenmiş Çay Fiyatı:", tea_with_sugar.cost())

    tea_with_milk = MilkDecorator(simple_tea)
    print("Süt Eklenmiş Çay Fiyatı:", tea_with_milk.cost())

    tea_with_sugar_and_milk = MilkDecorator(tea_with_sugar)
    print("Şeker ve Süt Eklenmiş Çay Fiyatı:", tea_with_sugar_and_milk.cost())


