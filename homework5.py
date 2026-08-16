from abc import ABC, abstractmethod 

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"[EMAIL] {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"[PUSH] {message}")

class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")


factory = NotificationFactory()
factory.create_notification("email").send("Hello!")
factory.create_notification("sms").send("Code: 1234")
factory.create_notification("push").send("New message!")

class UIFactory(ABC):
    @abstractmethod
    def button(self):
        pass
    @abstractmethod
    def input(self):
        pass

class LightButton:
    def display(self): 
        print("Light Button")

class LightInput:
    def display(self): 
        print("Light Input")

class LightFactory(UIFactory):
    def button(self): 
        return LightButton()
    def input(self): 
        return LightInput()

class DarkButton:
    def display(self): 
        print("Dark Button")
class DarkInput:
    def display(self): 
        print("Dark Input")
class DarkFactory(UIFactory):
    def button(self): 
        return DarkButton()
    def input(self): 
        return DarkInput()

factory = LightFactory()
factory.button().display()
factory.input().display()


class AudioProcessor:
    def process(self, file):
        print(f"Processing audio file: {file}")

class VideoProcessor:
    def process(self, file):
        print(f"Processing video file: {file}")

class ImageProcessor(ABC):
    def process(self, file):
        print(f"Processing image file: {file}")

class MediaFacade:
    @staticmethod
    def process(file, media_type):
        if media_type == "audio":
            AudioProcessor().process(file)
        elif media_type == "video":
            VideoProcessor().process(file)
        elif media_type == "image":
            ImageProcessor().process(file)
        else:
            raise ValueError(f"Unknown media type: {media_type}")

    
class Warrior(ABC):
    @abstractmethod
    def info(self):
        pass

class Mage(ABC):
    @abstractmethod
    def info(self):
        pass

class HumanWarrior(Warrior):
    def info(self):
        print("Human Warriror: HP = 120, Attack = 12, Mana = 5")

class HumanMage(Mage):
    def info(self):
        print("Human Mage: HP=80, Attack=8, MANA=20") 

  

class ElfWarrior(Warrior):
    def info(self):
        print("Elf Warrior: HP = 100, Attack = 13, Mana = 7")  

class ElfMage(Mage):
    def info(self):
        print("Elf Mage: HP=70, Attack=9, MANA=25")

class FractionFactory(ABC):
    @abstractmethod
    def create_warrior(self):
        pass

    @abstractmethod
    def create_mage(self):
        pass

          

class HumanFactory(FractionFactory):
    def create_warrior(self):
        return HumanWarrior()

    def create_mage(self):
        return HumanMage()

class ElfFactory(FractionFactory):
    def create_warrior(self):
        return ElfWarrior()

    def create_mage(self):
        return ElfMage()
