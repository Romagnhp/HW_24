# создание класса book
class Book:
    def __init__(self, name, year, publisher, genre, author ) -> None:
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.__price = None

# метод класса для изменения закрытого свойства price
    def setPrice(self,value):
        self.__price = value

# метод класса для обращения к закрытому значению свойства price
    def getPrice(self):
        return self.__price

# перегрузка метода __str__
    def __str__(self) -> str:
        return f"\nName - {self.name} \nPublisher - {self.publisher} \nYear - {self.year} \nGenre - {self.genre} \nAuthor - {self.author} \nPrice - {self.__price} UERO\n"

# создание объекта класса Book
book1 = Book("Atlas Shrugged", " Bobbs-Merrill Company", 1957, ["since fiction", "romance", "mystery"], "Ayn Rand")

print(book1)

# изменение значения свойства price
if book1.getPrice() == None:
    temp = int(input("Укажите цену = "))
    book1.setPrice(temp)

while True:
    if book1.getPrice() > 500:
        print("Стоимость превышает допустимую")
        temp = int(input("Укажите цену = "))
        book1.setPrice(temp)
    elif book1.getPrice() > 0 and book1.getPrice() < 500:
        print("Цена приемлимая\n")
        break
    else:
        print("Некорректоное значение цены")
        temp = int(input("Укажите цену = "))
        book1.setPrice(temp)

print(book1)
