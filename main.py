from Employee import Employee
from Person import Person
from Car import Car
from Office import Office


# Test Person Class
person = Person("Ashraf", 50000, "happy", 80)

person.sleep(1)
print(person.mood) 

person.eat(2)
print(person.health_rate) 

person.buy(3)
print(person.money) 

# Test Employee Class
employee = Employee("Ashraf", 2000, "happy", 90, 1, Car("Skoda", 10, 60), "ashraf@elshazlii.com", 5000, 20)
employee2 = Employee("Ahmed", 2000, "happy", 90, 1, Car("Skoda", 10, 60), "ashraf@elshazlii.com", 5000, 20)

employee.work(8)
print(employee.mood)

employee.drive(50)

employee.car.add_fuel(30)
print(employee.car.fuel_rate)

employee.send_mail()

# Test Office Class
office = Office("A Company")

office.hire(employee)    # Employee 1
office.hire(employee2)   # Employee 2
print(office.employees_num)

employees = office.get_all_employees()
for emp in employees:
    print(emp.name)

office.fire(1)
print(office.employees_num)

office.deduct(1, 200)
print(employee.salary)

office.reward(1, 300)
print(employee.salary)

office.check_lateness(1, 9)

# Test Car class
car = Car("Honda", 8, 70)

car.run(100, 70)

car.add_fuel(20)
print(car.fuel_rate)
