# Alt sistem bileşeni 1 - Televizyon
class TV:
    def turn_on(self):
        print("Televizyon açıldı.")

    def turn_off(self):
        print("Televizyon kapatıldı.")

# Facade 
class TVRemote:
    def __init__(self):
        self.tv = TV()

    def turn_on_tv(self):
        self.tv.turn_on()

    def turn_off_tv(self):
        self.tv.turn_off()

if __name__ == "__main__":
    remote = TVRemote()

    print("Televizyonu açma işlemi:")
    remote.turn_on_tv()

    print("Televizyonu kapatma işlemi:")
    remote.turn_off_tv()

