
# class for creating and writing files
class Writer:

    # A function that initially writes 
    # the name and data parameters
    def __init__(self, name, data):
        self.name = name
        self.data = data

    # A function that takes parameters from __init__
    # and create and write file
    def write(self):
        with open(f'{self.name}.md', 'w') as file:
            file.write(str(self.data))
