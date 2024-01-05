from Person import Person

class Employee(Person):
    def __init__(self, name, money, mood, health_rate, id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, gas_amount=100):
        self.car.add_fuel(gas_amount)

    def send_mail(self):
        email = self.email
        print("Email has been sent")

    def adjust_salary(self, move_hour):
        target_hour = 9 
        distance = self.distance_to_work
        velocity = self.car.velocity

        if self.office.calculate_lateness(target_hour, move_hour, distance, velocity):
            self.salary -= 10
        else:
            self.salary += 10