from vehicle import Vehicle

class Car(Vehicle):
    
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


accord = Car(30, 4)
print(accord.go())
print(accord.wheel_size)