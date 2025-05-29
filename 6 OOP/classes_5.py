class MultiplierFactory():
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, value):
        return self.multiplier * value

    def __repr__(self):
        return f"Multiplier(n={self.multiplier})"


# double = MultiplierFactory(2)
# triple = MultiplierFactory(3)
#
# print(double(10))  # 20
# print(triple(5))   # 15
#
# print(repr(double))  # Multiplier(n=2)

class KeyValueStorage:
    def __init__(self):
        object.__setattr__(self, 'storage', {})

    def __getitem__(self, key):
        return self.storage[key]

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getattr__(self, key):
        if key in self.storage:
            return self.storage[key]
        raise AttributeError(f"No such attribute: {key}")

    def __setattr__(self, key, value):
        if key == 'storage':
            object.__setattr__(self, key, value)
        else:
            self.__setitem__(key, value)

    def __contains__(self, key):
        return key in self.storage

    def __repr__(self):
        return repr(self.storage)




kv = KeyValueStorage()
kv['name'] = 'Alice'
kv.age = 30

print(kv['age'])     # 30
print(kv.name)       # 'Alice'
print('name' in kv)  # True
print(kv)            # {'name': 'Alice', 'age': 30}