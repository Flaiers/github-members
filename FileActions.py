
# class for creating and writing files
class Writer:

    # A function that initially writes 
    # the name and data parameters
    def __init__(self, name: str, date, data):
        self.name = name
        self.date = date
        self.data = data

    # A function that takes parameters from __init__
    # and create and write file
    def write(self) -> None:
        with open(f'{self.name}.txt', 'w') as file:
            file.write('Writed on %s\n\n' % self.date)
            file.write(str(self.data))
