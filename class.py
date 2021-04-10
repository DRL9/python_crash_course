class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is now rolling")


dog = Dog(name="Mark", age=10)
dog.sit()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

    def fill_gas_tank(self):
        print(f"filling {self.get_descriptive_name()}")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 调用父类的 init
        super().__init__(make, model, year)

    # 重写
    def fill_gas_tank(self):
        print("This car doesn't need a get tank")


tesla = ElectricCar(make="chinese", model="hongqi", year=2020)
print(tesla.get_descriptive_name())
tesla.fill_gas_tank()
