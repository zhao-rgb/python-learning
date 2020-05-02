"""
使用 @property 装饰类属性

"""

class Book(object):
    def __init__(self, name, sale):
        self.__name = name
        self.__sale = sale

    @property
    def name(self):
        return self.__name

a_book = Book('magic_book', 100000)
print(a_book.name)