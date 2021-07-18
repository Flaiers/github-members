
# importing myClass
from FileActions import Writer
from GettingData import GenerateTable


# run my files
print("_________________________Runner loaded__________________________")
object = GenerateTable('https://github.com/')
object.getMyData()
w = Writer('output', object.table)
w.write()
