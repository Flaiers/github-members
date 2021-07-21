
# importing myClasses
from FileActions import Writer
from GettingData import GenerateTable


# run parsing and database saving
print("_________________________Runner loaded__________________________")
object = GenerateTable('github') # If you don't want save to the database
                                 # GenerateTable('github', False)
object.getMyData()
w = Writer('output', object.table)
w.write()
