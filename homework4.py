from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def __str__(self):
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Invalid card number. It must be a 16-digit number.")
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f} using card number {self.card_number[-4:]}.")   

    def __str__(self):
        return f"Credit Card Payment (Card Number: {self.card_number})"

class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        if "@" not in email:
            raise ValueError("Invalid email address.")
        self.email = email

    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f} using email {self.email}")

    def __str__(self):
        return f"PayPalPayment(email={self.email})"   

class CryptoPayment(PaymentMethod):
    def __init__(self, wallet):
        if len(wallet) < 10:
            raise ValueError("Invalid wallet address. It must be at least 10 characters long.")
        self.wallet = wallet

    def process_payment(self, amount):
        print(f"Processing crypto payment of ${amount:.2f} using wallet {self.wallet}")

    def __str__(self):
        return f"CryptoPayment(wallet={self.wallet})"      




class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __repr__(self):
        return f"{self.__class__.__name__}(area={self.area():.2f})"


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError(" Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(" The sum of any two sides must be greater than the third side")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

