# A class is a collection of instance variables and related methods
from abc import ABC, abstractmethod


class Book(ABC):

    # The __init__ special method, also known as a Constructor, is used to initialize the class with attributes
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        # Private attributes are inaccessible attributes use getter and setter methods to access private attributes
        self.__price = price
        self.__discount = None

    # Magic / special method 
    @abstractmethod
    def __repr__(self) -> str:
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()} "

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price


# A class's ability to inherit methods and/or characteristics from another class is known as inheritance.

class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

        # Polymorphism (a subclass can use a method from its superclass as is or modify it as needed.)

    def __repr__(self) -> str:
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}, Pages: {self.pages} "


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    # Polymorphism
    def __repr__(self) -> str:
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()} "


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)
