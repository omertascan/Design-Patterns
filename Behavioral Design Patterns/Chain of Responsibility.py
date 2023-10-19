from abc import ABC, abstractmethod

# Handler (İşlemci) arayüzü
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

# ConcreteHandler (Somut İşlemciler)
class ConcreteHandlerA(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request == "A":
            print("ConcreteHandlerA işlemi gerçekleştiriyor.")
        elif self.successor is not None:
            self.successor.handle_request(request)

class ConcreteHandlerB(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request == "B":
            print("ConcreteHandlerB işlemi gerçekleştiriyor.")
        elif self.successor is not None:
            self.successor.handle_request(request)

class ConcreteHandlerC(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request == "C":
            print("ConcreteHandlerC işlemi gerçekleştiriyor.")
        elif self.successor is not None:
            self.successor.handle_request(request)

# İstemci (Client)
if __name__ == "__main__":
    handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC()))

    requests = ["A", "B", "C", "D"]

    for request in requests:
        handler_chain.handle_request(request)
