# doesn't work :(
class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner is not None:
            return 'Car already sold'

        if money >= self.price:
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {money - self.price}'
        else:
            return 'Sorry, not enough money'

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return 'Vehicle has no owner'

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle)
print(vehicle.buy(50000, 'turutu'))
print(vehicle)
print(vehicle.buy(50000, 'hashmasha'))
vehicle.sell()
print(vehicle)
