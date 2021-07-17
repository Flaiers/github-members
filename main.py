
# importing myClass
from FileActions import Writer
from GettingData import GenerateTable

# Entry Point
if __name__ == '__main__':
    object = GenerateTable()
    object.getData('https://github.com/')
    w = Writer('output', object.table)
    w.write()
