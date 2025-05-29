def sum_all(*args):
    if args:
        print(sum(args))
    else:
        print(0)

sum_all(1, 2, 3)  # → 6
sum_all()

def greet(name: str, age=18):
    print(f'Hello, {name}! You are {age} years old.')

greet("Alice")             # → Hello, Alice! You are 18 years old.
greet("Bob", age=25)       # → Hello, Bob! You are 25 years old.
greet(name="Charlie")      # → Hello, Charlie! You are 18 years old.

def print_keys(**kwargs):
    for key, value in kwargs.items():
        if type(value) == str:
            print(key)

print_keys(name="Alice", age=30, city="Paris")

def add_item(val, list : list = None):
    if list:
        return list.append(val)
    else:
        return [val]

print(add_item("a"))
print(add_item("b"))