class Office:
    employees_num = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def hire(self, employee):
        employee.office = self 
        self.employees.append(employee)

    def fire(self, id):
        for employee in self.employees:
            if employee.id == id:
                self.employees.remove(employee)
                break

    def get_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None

    def deduct(self, id, deduction):
        employee = self.get_employee(id)
        if employee:
            employee.salary -= deduction

    def check_lateness(self, id, move_hour):
        employee = self.get_employee(id)
        if employee:
            employee.adjust_salary(move_hour)
        else:
            print("Employee not found.")

    def reward(self, id, reward):
        employee = self.get_employee(id)
        if employee:
            employee.salary += reward

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        if move_hour < target_hour:
            return False

        travel_time = distance / velocity
        arrival_hour = move_hour + travel_time

        if arrival_hour <= target_hour:
            return False
        else:
            return True
