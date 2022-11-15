# Создание класса Car
class Car:
    def __init__(self, model, year, manufacturing, engineCapacity, price) -> None:
        self.model = model
        self.year = year
        self.manufacturing = manufacturing
        self.engineCapacity = engineCapacity
#закрытое свойство color .        
        self.__color = "white"
        self.price = price

# метод класса, для изменения свойства color
    def setColor(self,value):
        self.__color = value

# метод класса для обращения к закрытому значению color    
    def getColor(self):
        return self.__color
  
# перегрузка магического метода  __str__, базового класса Object
    def __str__(self) -> str:
        return f"\nModel - {self.model} \nYear - {self.year} \nManufacturing - {self.manufacturing} \nCapaciti of engine - {self.engineCapacity} л \nColor - {self.__color}\nPrice - {self.price} EURO \n"  

# создание объекта класса Car
car1 = Car("Rapid", 2019, "Skoda", 1.6, 500)

print(car1)

n = input("Введите желаемый цвет авто = ")
car1.setColor(n)

# Если цвет авто не белый добавить к цене авто 10%
if not car1.getColor() == "white":
    car1.price = car1.price + (car1.price * 0.1)
    
print(car1)
