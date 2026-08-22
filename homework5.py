from abc import ABC, abstractmethod 

class Notification_Creator(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def send(self, message):
        notification = self.create_notification()
        notification.send(message)

class Email_Creator(Notification_Creator):
    def create_notification(self):
        return Email_Notification()


class SMS_Creator(Notification_Creator):
    def create_notification(self):
        return SMS_Notification()


class Push_Creator(Notification_Creator):
    def create_notification(self):
        return Push_Notification()

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class Email_Notification(Notification):
    def send(self, message: str):
        print(f"[EMAIL] {message}")


class SMS_Notification(Notification):
    def send(self, message: str):
        print(f"[SMS] {message}")


class Push_Notification(Notification):
    def send(self, message: str):
        print(f"[PUSH] {message}")

def client_code(creator: Notification_Creator):
    creator.send("Hello!")

client_code(Email_Creator())
client_code(SMS_Creator())
client_code(Push_Creator())


class Button(ABC):
    @abstractmethod
    def display(self):
        pass

class Input(ABC):
    @abstractmethod
    def display(self):
        pass

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_input(self):
        pass

class LightButton(Button):
    def display(self): 
        print("Light Button")

class LightInput(Input):
    def display(self): 
        print("Light Input")

class LightFactory(UIFactory):
    def create_button(self):
        return LightButton()
    def create_input(self):
        return LightInput()

class DarkButton(Button):
    def display(self): 
        print("Dark Button")
class DarkInput(Input):
    def display(self): 
        print("Dark Input")
class DarkFactory(UIFactory):
    def create_button(self): 
        return DarkButton()
    def create_input(self): 
        return DarkInput()

factory = LightFactory()
factory.create_button().display()
factory.create_input().display()


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
