class Car:
    def __init__(self, model, year, manufacturing, engineCapacity, color) -> None:
        self.model = model
        self.year = year
        self.manufacturing = manufacturing
        self.engineCapacity = engineCapacity
        self.color = color
        self.__price = None

    def setPrice(self,value):
        self._price = value

    def getPrice(self):
        return self._price

# метод для вывода данных
    def __str__(self) -> str:
        return f"Model - {self.model} \nYear - {self.year} \nManufacturing - {self.manufacturing} \nCapaciti of engine - {self.engineCapacity} \nColor - {self.color} \n"  

car1 = Car("Rapid", 2019, "Skoda", 1.6, "white")

print(car1)
n =input("\nВведите цену авто = ")
car1.setPrice(n)
print(f"Price =  {car1.getPrice()}")
print(car1)
