from abc import ABC, abstractmethod

# AbstractClass 
class DocumentTemplate(ABC):
    def create_document(self):
        self.add_title()
        self.add_content()
        self.add_footer()

    @abstractmethod
    def add_title(self):
        pass

    @abstractmethod
    def add_content(self):
        pass

    def add_footer(self):
        print("Altbilgi eklendi.")

# ConcreteClass 
class ResumeDocument(DocumentTemplate):
    def add_title(self):
        print("Özgeçmiş Başlığı Eklendi.")

    def add_content(self):
        print("Özgeçmiş İçeriği Eklendi.")

class ReportDocument(DocumentTemplate):
    def add_title(self):
        print("Rapor Başlığı Eklendi.")

    def add_content(self):
        print("Rapor İçeriği Eklendi.")

if __name__ == "__main__":
    resume = ResumeDocument()
    report = ReportDocument()

    print("Özgeçmiş Oluşturma:")
    resume.create_document()

    print("\nRapor Oluşturma:")
    report.create_document()


