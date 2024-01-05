class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self._fuel_rate = fuel_rate
        self._velocity = velocity

    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        if value < 0 or value > 100:
            raise ValueError("Fuel rate must be between 0 and 100.")
        self._fuel_rate = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if value < 0 or value > 200:
            raise ValueError("Velocity must be between 0 and 200.")
        self._velocity = value

    def run(self, distance, velocity):
        fuel_needed = distance * self._fuel_rate
        if fuel_needed > self._fuel_rate:
            print("Not enough fuel to complete the distance.")
            distance_covered = self._fuel_rate / self._fuel_rate
        else:
            distance_covered = distance
        print(f"Car {self.name} has covered {distance_covered} km at {velocity} km/h.")

    def add_fuel(self, amount):
        if amount < 0 or self._fuel_rate + amount > 100:
            raise ValueError("Invalid fuel amount.")
        self._fuel_rate += amount
