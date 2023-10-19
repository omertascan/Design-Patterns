# Originator sınıfı
class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def save(self):
        return TextMemento(self.text)

    def restore(self, memento):
        self.text = memento.get_text()

# Memento sınıfı
class TextMemento:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

# Caretaker sınıfı
class History:
    def __init__(self):
        self.states = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        if self.states:
            return self.states.pop()
        return None

if __name__ == "__main__":
    text_editor = TextEditor()
    history = History()

    text_editor.write("Bu bir metin.")
    history.push(text_editor.save())

    text_editor.write(" Yeni metin ekleniyor.")
    history.push(text_editor.save())

    text_editor.write(" Daha fazla metin ekleniyor.")
    print("Şu anki metin:", text_editor.text)

    # Geri alma
    last_state = history.pop()
    if last_state:
        text_editor.restore(last_state)
        print("Geri alındı:", text_editor.text)

    # Bir daha geri al
    last_state = history.pop()
    if last_state:
        text_editor.restore(last_state)
        print("Bir daha geri alındı:", text_editor.text)

