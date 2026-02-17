class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, rest_days):
        hours = (7 - rest_days) * 8
        return hours
    
    @classmethod
    def get_email(cls, name):
        email = f"{name}@email.com"
        return email
    
    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment
    
# ---------- ПРОВЕРКА ----------
# 1) создаём сотрудника "из данных"
emp = EmployeeSalary(name="ivan", hours=40, rest_days=2, email="ivan@email.com")
print("salary:", emp.salary())          # 40 * 400 = 16000
print("email:", emp.email)

# 2) проверяем classmethod-ы
print("hours by rest_days=2:", EmployeeSalary.get_hours(2))  # (7-2)*8 = 40
print("email by name:", EmployeeSalary.get_email("petr"))    # petr@email.com

# 3) меняем ставку и смотрим, как изменилась зп
EmployeeSalary.set_hourly_payment(500)
print("salary after raise:", emp.salary())  # 40 * 500 = 20000

# 4) пример создания сотрудника “правильным способом” через вычисления
name = "anna"
rest_days = 3
hours = EmployeeSalary.get_hours(rest_days)
email = EmployeeSalary.get_email(name)
emp2 = EmployeeSalary(name=name, hours=hours, rest_days=rest_days, email=email)
print("emp2:", emp2.name, emp2.hours, emp2.rest_days, emp2.email, "salary:", emp2.salary())