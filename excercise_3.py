# создание класса Stedium
class Stedium:
    def __init__(self, name, date, country, city) -> None:
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.__capacity = 0

# метод класса для изменения закрытого свойства __capacity
    def setCapacity(self, value):
        self.__capacity = value

# метод класса для обращения к закрытому значению свойства __capacity
    def getCapacity(self):
        return self.__capacity

# перегрузка метода __str__
    def __str__(self) -> str:
        return f"Name - {self.name} \nDate - {self.date} \nCountry - {self.country} \nCity - {self.city} \nCapacity - {self.__capacity} человек\n"

# создание объекта класса Stedium
stedium1 = Stedium("Wembley", 2007, "Great Britain", "London")


while True:
    if stedium1.getCapacity() < 1000000 and stedium1.getCapacity() > 100:
        break
    else:
        n = int(input("Введите корректное значение вместимости стадиона = "))
        stedium1.setCapacity(n)
    
print(stedium1)
