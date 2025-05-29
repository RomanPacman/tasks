class FunctionLogger():
    count = 0

    def __call__(self, wrapper):
        def func(
                wrapper):
            return wrapper






@FunctionLogger
def add(a, b):
    return a + b

add(2, 3)   # Лог: вызов add(2, 3)
add(5, 7)   # Лог: вызов add(5, 7)

print(add.count())  # 2