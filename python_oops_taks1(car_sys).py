class Car:
    def __init__(self,make,model,year,color,_speed,accelerate,brea_k):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self._speed=_speed
        self.accelerate=accelerate
        self.brea_k=brea_k

    def start(self):
        print(f"car is starting")

    def speedd(self):
        print("f car speed is " ,{self._speed})

    def acceleratee(self):
        print("f accelerate increased to ", {self.accelerate})

    def breakk(self):
        print("f speed decreased to ",{self.brea_k})

    def stop(self):
        print(f"car is stopping")

    def display_info(self):
        print(f"{self.make},{self.model},{self.year},{self.color}")



c=Car("TATA","TATA_CURVE","2022","GREEN",70,90,10)
# print(c.make("Toyota"))
print(c.start())
print(c.stop())
print(c.display_info())
print(c.speedd())
print(c.acceleratee())
print(c.breakk())

print("------------own written code ------------------------")




class Car:
    def __init__(self, make, model, year, color, speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed  # Current speed of the car

    def start(self):
        print("Car is starting.")

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}")

    def speed_info(self):
        print(f"Current speed is {self.speed} km/h.")

    def accelerate(self, increase_speed):
        self.speed += increase_speed
        print(f"Speed increased to {self.speed} km/h.")

    def brake(self, decrease_speed):
        self.speed -= decrease_speed
        print(f"Speed decreased to {self.speed} km/h.")

    def stop(self):
        print("Car is stopping.")
        self.speed = 0  # Speed is set to 0 when the car stops
        print(f"Car stopped. Speed is now {self.speed} km/h.")


# Create a Car object
c = Car("TATA", "TATA_CURVE", 2022, "Green", 70)

# Calling methods on the car object
c.start()
c.display_info()
c.speed_info()
c.accelerate(20)  # Accelerate the car by 20 km/h
c.brake(10)  # Brake the car by 10 km/h
c.stop()





