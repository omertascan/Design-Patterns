import copy

class Prototype:
    def clone(self):
        # __dict__ ile nesne özellikleri kopyalanır
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"ConcretePrototype with value: {self.value}")

# İlk nesne oluşturulur
original = ConcretePrototype("Original")

# Orijinal nesnenin kopyası oluşturulur
clone1 = original.clone()
clone1.show()

# Orijinal nesnenin farklı bir kopyası oluşturulur
clone2 = original.clone()
clone2.show()

# Kopyalanan nesnelerin aynı özelliklere sahip olduğu kontrol edilir
print(clone1.value == clone2.value)  # True
