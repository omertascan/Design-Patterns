from abc import ABC, abstractmethod

# Element 
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# ConcreteElement 
class TextElement(Element):
    def accept(self, visitor):
        visitor.visit_text(self)

class ImageElement(Element):
    def accept(self, visitor):
        visitor.visit_image(self)

# Visitor 
class Visitor(ABC):
    @abstractmethod
    def visit_text(self, element):
        pass

    @abstractmethod
    def visit_image(self, element):
        pass

# ConcreteVisitor 
class StatisticsVisitor(Visitor):
    def visit_text(self, element):
        print("Metin öğesi analiz edildi.")

    def visit_image(self, element):
        print("Görsel öğesi analiz edildi.")

# ObjectStructure 
class Document:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

if __name__ == "__main__":
    # Örnek bir belge oluşturuluyor ve öğeler ekleniyor
    document = Document()
    document.add_element(TextElement())
    document.add_element(ImageElement())

    # İstatistikleri hesaplayan bir ziyaretçi oluşturuluyor
    statistics_visitor = StatisticsVisitor()

    # Belgedeki öğeleri gezerek ziyaretçiye kabul ettiriliyor
    document.accept(statistics_visitor)


