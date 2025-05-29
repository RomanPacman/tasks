class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, data_string:str):
        data_list = data_string.split(';')
        return cls(data_list[0] , data_list[1])

    def description(self):
        print(f'{self.title} by {self.author}')

b = Book.from_string("1984;George Orwell")
b.description()