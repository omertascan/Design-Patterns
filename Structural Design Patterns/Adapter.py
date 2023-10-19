# Hedef Arabirim (Target)
class Socket:
    def plug_in(self):
        pass

# Adapte Edilen (Adaptee)
class Kettle:
    def plug(self):
        print("Çaydanlık prize takıldı.")

# Adaptör (Adapter)
class KettleAdapter(Socket):
    def __init__(self, kettle):
        self.kettle = kettle

    def plug_in(self):
        self.kettle.plug()

if __name__ == "__main__":
    kettle = Kettle()
    adapter = KettleAdapter(kettle)
    adapter.plug_in()


