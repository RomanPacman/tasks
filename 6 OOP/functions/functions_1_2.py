def describe_person(*args, **kwargs):
    if 'name' in kwargs and 'age' in kwargs:
        print(f"{kwargs['name']} is {kwargs['age']} years old.")
    if len(args) > 0:
        print(f"Qualities: {str(args).split(', ')}")




# describe_person("brave", "kind", "smart", name="John", age=30)

def check_conflict(name, **kwargs):
    if 'name' in kwargs:
        raise TypeError("Conflict: 'name' given twice")
    else:
        print(f"Hello, {name}!")

# check_conflict("Alice")                        # Hello, Alice!
# check_conflict(name="Bob")                     # Hello, Bob!
# check_conflict("Alice", name="Bob")            # ❌ TypeError: Conflict: 'name' given twic



def square(x): return x * x


def apply_twice(sup_func, val):
    return sup_func(sup_func(val))

# print(apply_twice(square, 2))  # → 16 (т.к. square(square(2)) → square(4) → 16)

def make_multiplier(mul):
    return '??'


double = make_multiplier(2)
triple = make_multiplier(3)

# print(double(5))  # → 10
# print(triple(4))  # → 12

class Test():
    pass


import this


# a_ = this
# a_.s
# print(a_.d)

