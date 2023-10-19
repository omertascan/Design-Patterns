from abc import ABC, abstractmethod

# State 
class State(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# ConcreteState 
class OnState(State):
    def turn_on(self):
        print("Lamba zaten açık.")

    def turn_off(self):
        print("Lamba kapatılıyor.")
        # Durumu değiştirerek lambayı kapat
        self.context.transition_to(OffState())

class OffState(State):
    def turn_on(self):
        print("Lamba açılıyor.")
        # Durumu değiştirerek lambayı aç
        self.context.transition_to(OnState())

    def turn_off(self):
        print("Lamba zaten kapalı.")

# Context 
class Lamp:
    def __init__(self):
        # Başlangıçta lamba kapalı durumdadır
        self._state = OffState()
        self._state.context = self  # Duruma erişim için context'i ayarla

    def transition_to(self, state):
        self._state = state
        self._state.context = self  # Duruma erişim için context'i ayarla

    def turn_on(self):
        self._state.turn_on()

    def turn_off(self):
        self._state.turn_off()

if __name__ == "__main__":
    lamp = Lamp()

    lamp.turn_on()  # Lambayı aç
    lamp.turn_on()  # Açık lambayı açmaya çalış
    lamp.turn_off()  # Lambayı kapat
    lamp.turn_off()  # Kapalı lambayı kapatmaya çalış
