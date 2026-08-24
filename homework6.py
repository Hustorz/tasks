from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self, data):
        pass

class BasicReport(Report):
    def generate(self, data):
        return f"Basic Report: {data}"


class ReportDecorator(Report):
    def __init__(self, report):
        self._report = report

    @abstractmethod
    def generate(self, data):
        pass

class PDFReportDecorator(ReportDecorator):
    def generate(self, data):
        base_report = self._report.generate(data)
        return f"{base_report} [PDF Format]"

class ExcelReportDecorator(ReportDecorator):
    def generate(self, data):
        base_report = self._report.generate(data)
        return f"{base_report} [Excel Format]"

class SignatureReportDecorator(ReportDecorator):
    def generate(self, data):
        base_report = self._report.generate(data)
        return f"{base_report} [Signed]"

def client_code(report: Report, data):
    print(report.generate(data))

print("\nPDF + Signature Report:")
r1 = SignatureReportDecorator(PDFReportDecorator(BasicReport()))
client_code(r1, 'Hello!')



class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass
    @abstractmethod
    def detach(self, observer: Observer):
        pass
    @abstractmethod
    def notify(self, event: str):
        pass  

class MonitoringServer(Subject):
    def __init__(self):
        self._observers = []
    def attach(self, observer: Observer):
        self._observers.append(observer)
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    def notify(self, event: str):
        for observer in self._observers:
            observer.update(event)
    def highCPU(self):
        print("High CPU usage detected!")
        self.notify("High CPU usage")
    def MemoryNotEnough(self):
        print("Memory not enough detected!")
        self.notify("Memory not enough")
    def ServiceUnavailable(self):
        print("Service unavailable detected!")
        self.notify("Service unavailable")    

class Observer(ABC):
    @abstractmethod
    def update(self, event: str):
        pass

class EmailNotifier(Observer):
    def update(self, event: str):
        print(f'[Email]: {event}')  

class TelegramNotifier(Observer):
    def update(self, event: str):
        print(f'[Telegram]: {event}')

class LogWriter(Observer):
    def update(self, event: str):
        print(f'[Log]: {event} recorded')


def client_code():
    server = MonitoringServer()
    email = EmailNotifier()
    telegram = TelegramNotifier()
    log = LogWriter()
    server.notify(email)
    server.attach(telegram)
    server.attach(log)

    server.highCPU()

client_code()


class Context(ABC):
    def __init__(self, weight: float, distance: float, strategy: Strategy):
        self._strategy = strategy 
        self._weight = weight 
        self._distance = distance

    @property
    def strategy(self) -> Strategy: 
        return self._strategy 
    @strategy.setter 
    def strategy(self, strategy: Strategy):
        self._strategy = strategy
        

    def bussines_logic(self):
        return self._strategy.cost_calculation(self._weight, self._distance) 

class Strategy(ABC): 
    @abstractmethod
    def cost_calculation(self, weight: float, distance: float) -> float:
        pass
class RoadDelivery(Strategy):
    def cost_calculation(self, weight, distance) -> float:
        return weight * distance
class AirDelivery(Strategy):
    def cost_calculation(self, weight, distance) -> float:
        return weight**2 * distance
class WaterDelivery(Strategy):
    def cost_calculation(self, weight, distance) -> float:
        return weight * distance/6

def client_code():
    delivery = Context(weight = 2000, distance = 1400, strategy = AirDelivery())
    print(f'Road Delivery - {delivery.bussines_logic()}')
    delivery.strategy = AirDelivery()
    print("Air Delivery:", delivery.bussines_logic())

    delivery.strategy = WaterDelivery()
    print("Water Delivery:", delivery.bussines_logic())
    delivery._weight = 500
    delivery._distance = 300

    delivery.strategy = RoadDelivery()
    print("Road Delivery:", delivery.bussines_logic())

client_code()

        

    

    


