# Observer 
class Observer:
    def update(self, temperature, humidity):
        pass

# Subject
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_weather_data(self, temperature, humidity):
        self._temperature = temperature
        self._humidity = humidity
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

# ConcreteObserver 
class WeatherDisplay(Observer):
    def update(self, temperature, humidity):
        print(f"Hava Durumu Güncellendi - Sıcaklık: {temperature}°C, Nem: {humidity}%")

if __name__ == "__main__":
    weather_station = WeatherStation()

    observer1 = WeatherDisplay()
    observer2 = WeatherDisplay()

    weather_station.add_observer(observer1)
    weather_station.add_observer(observer2)

    weather_station.set_weather_data(25, 60)
    weather_station.set_weather_data(28, 55)

