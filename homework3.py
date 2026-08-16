import time
from functools import wraps


def desk_to_graph(n):
    graph = { (i, j): {(k, l) for k in range(1, n+1) for l in range(1, n+1) if abs(i - k) + abs(j - l) == 3 and i != k and j != l} for i in range(1, n+1) for j in range(1, n+1)}
    return graph

path = []

def dfs_chess(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    path.append(start)

    if len(path) == len(graph):
        return True

    for neighbor in graph[start] - visited:
        if dfs_chess(graph, neighbor, visited):
            return True
    visited.remove(start)
    path.pop()
    return False
        
         
    
employees = [
    {"name": "Kirill", "hours": 160, "rate": 12, "bonus_percent": 10, "tax_percent": 13},
    {"name": "Masha",   "hours": 165, "rate": 15, "bonus_percent": 5,  "tax_percent": 20},
]


def salary_calc(employees):
    return [employee["hours"] * employee["rate"] for employee in employees]
bonus_percent = lambda p: p / 100

def calc_bonus(employees, base_salaries):
    return [
        base * bonus_percent(emp["bonus_percent"])
        for base, emp in zip(base_salaries, employees)
    ]

def calc_tax(employees, base_salaries, bonuses):
    return [
        (base + bonus) * emp["tax_percent"] / 100
        for base, bonus, emp in zip(base_salaries, bonuses, employees)
    ]
def calc_total_payment(base_salaries, bonuses, taxes):
    return [
        base + bonus - tax
        for base, bonus, tax in zip(base_salaries, bonuses, taxes)
    ]

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n===function: {func.__name__} ===")

        start_time = time.time()
        print(f"beginning: {start_time:.5f}")

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time

        print(f"duration: {duration:.5f} seconds")
        print(f"return value: {result}")

        return result
    return wrapper


@log_execution
def add(a, b):
    return a + b
@log_execution
def dfs_chess(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    path.append(start)

    if len(path) == len(graph):
        return True

    for neighbor in graph[start] - visited:
        if dfs_chess(graph, neighbor, visited):
            return True
    visited.remove(start)
    path.pop()
    return False

@log_execution
def min_max(lst):
    return min(lst), max(lst)   

class Book: 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property 
    def pages(self):
        return self.__pages

    @title.setter
    def title(self, value):
        self.__title = value

    @author.setter
    def author(self, value):
        self.__author = value

    @pages.setter
    def pages(self, value):
        if value < 0:
            raise ValueError("Number of pages cannot be negative.")
        self.__pages = value
    def str(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


class Product:
    def Product(self, name, price):
        self.name = name
        self.price = price 
    def __str__(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}"
    def __len__(self):
        return len(self.name)
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False
    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        raise TypeError("Unsupported operand type for +: 'Product' and '{}'".format(type(other).__name__))
    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price > other.price
        raise TypeError("Unsupported operand type for >: 'Product' and '{}'".format(type(other).__name__))




    
    
    




    

