class Car:
    def __init__(self):
        self._speed=120

class SportsCar(Car):
    def show_speed(self):
        print("Speed:",self._speed)


car=SportsCar()
car.show_speed()
print(car._speed)