def greet(name: str) -> str:
    return f'Hello {name}!'
    # return 'Hello ' + name

def add(a: int, b: int = 0) -> int:
    return a + b

def min_max(numbers: list[int]) -> tuple[int, int]:
    return (min(numbers), max(numbers))


def total_sum(*args: int) -> int:
    return sum(args)


def print_named(**kwargs) -> str:
    list_items = [f'{k}={v}' for k,v in kwargs.items()]
    # for k,v in kwargs.items():
    #     list_items.append(f'{k}={v}')
    return ', '.join(list_items)

# print(print_named(a=1, b=2))

def make_power(n: int):
    return lambda i : i**n

square = make_power(2)
cube = make_power(3)

# print(square(4))
# print(cube(2))