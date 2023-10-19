# Implementor (Uygulayıcı) - Mesaj Gönderim
class MessageSender:
    def send_message(self, message):
        pass

# Concrete Implementor (Somut Uygulayıcı) - SMS
class SMSMessageSender(MessageSender):
    def send_message(self, message):
        print(f"SMS gönderiliyor: {message}")

# Concrete Implementor (Somut Uygulayıcı) - E-posta
class EmailMessageSender(MessageSender):
    def send_message(self, message):
        print(f"E-posta gönderiliyor: {message}")

# Abstraction (Soyutlama) - Mesaj
class Message:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        self.sender.send_message(message)

if __name__ == "__main__":
    sms_sender = SMSMessageSender()
    email_sender = EmailMessageSender()

    sms_message = Message(sms_sender)
    email_message = Message(email_sender)

    sms_message.send("Merhaba, bu bir SMS!")
    email_message.send("Merhaba, bu bir E-posta!")


