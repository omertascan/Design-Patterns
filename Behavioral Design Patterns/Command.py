from abc import ABC, abstractmethod

# Command arayüzü
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# ConcreteCommand sınıfları
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Receiver sınıfı
class Light:
    def turn_on(self):
        print("Işık açık")

    def turn_off(self):
        print("Işık kapalı")

# Invoker sınıfı
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

if __name__ == "__main__":
    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.set_command(light_on)
    remote.press_button()  # Işığı aç

    remote.set_command(light_off)
    remote.press_button()  # Işığı kapat