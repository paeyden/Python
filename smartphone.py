# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# Child class with encapsulation
class Smartphone(Device):
    def __init__(self, brand, model, battery_life):
        super().__init__(brand, model)
        self.__battery_life = battery_life  # private attribute (encapsulation)

    # Method to access private attribute
    def battery_status(self):
        return f"Battery life: {self.__battery_life} hours"

    # Method to simulate usage
    def use_phone(self, hours):
        if hours <= self.__battery_life:
            self.__battery_life -= hours
            return f"Used phone for {hours} hours. Remaining battery: {self.__battery_life} hours"
        else:
            return "Not enough battery!"

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 20)
phone2 = Smartphone("Samsung", "Galaxy S23", 25)

print(phone1.info())
print(phone1.battery_status())
print(phone1.use_phone(5))
print(phone1.use_phone(20))
