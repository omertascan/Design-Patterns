from abc import ABC, abstractmethod

# Mediator 
class Mediator(ABC):
    @abstractmethod
    def send_message(self, colleague, message):
        pass

# ConcreteMediator 
class ChatRoom(Mediator):
    def __init__(self):
        self.colleagues = []

    def add_colleague(self, colleague):
        self.colleagues.append(colleague)

    def send_message(self, colleague, message):
        for c in self.colleagues:
            if c != colleague:  # Kendi kendine mesaj gönderme
                c.receive_message(message)

# Colleague 
class Colleague(ABC):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive_message(self, message):
        pass

# ConcreteColleague 
class User(Colleague):
    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} receives: {message}")

if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User(chat_room, "User1")
    user2 = User(chat_room, "User2")
    user3 = User(chat_room, "User3")

    chat_room.add_colleague(user1)
    chat_room.add_colleague(user2)
    chat_room.add_colleague(user3)

    user1.send("Hello, everyone!")
    user2.send("Hi, User1!")
    user3.send("Hey there!")


