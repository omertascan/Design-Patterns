# Component 
class MusicComponent:
    def __init__(self, name):
        self.name = name

    def play(self):
        pass

# Leaf 
class Song(MusicComponent):
    def play(self):
        print(f"Şarkı çalınıyor: {self.name}")

# Composite 
class Playlist(MusicComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, child):
        self.children.append(child)

    def play(self):
        print(f"Playlist çalınıyor: {self.name}")
        for child in self.children:
            child.play()

if __name__ == "__main__":
    song1 = Song("Şarkı 1")
    song2 = Song("Şarkı 2")
    playlist = Playlist("Favori Şarkılar")

    playlist.add(song1)
    playlist.add(song2)

    playlist.play()

