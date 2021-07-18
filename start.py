
# importing myClass
from FileActions import Writer
from GettingData import GenerateTable


# run my files
print("_________________________Runner loaded__________________________")
object = GenerateTable('https://github.com/')
object.getData()
w = Writer('output', object.table)
w.write()
