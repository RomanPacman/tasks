class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return f"Employee: {self.name}, salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def info(self):
        return super().info() + f', manages team of {self.team_size}'



# e = Employee("Alice", 50000)
# print(e.info())     # "Employee: Alice, salary: 50000"
#
# m = Manager("Bob", 80000, 5)
# print(m.info())     # "Employee: Bob, salary: 80000, manages team of 5"


class User():
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, str_pass:str):
        return self.__password == str_pass

    def change_password(self, old_pass:str, new_pass:str):
        if self.check_password(old_pass):
            self.__password = new_pass
            print('Новый пароль установлен')
        else:
            print('Ошибка установки пароля')

    def __repr__(self):
        return f'User(username={self.username})'

u = User("admin", "1234")
print(u.check_password("1234"))   # True
u.change_password("1234", "5678")
print(u.check_password("5678"))   # True
print(repr(u))                    # User(username='admin')
