# import logging system and datetime
import logging

from datetime import datetime

# importing myClasses
from FileActions import Writer
from GettingData import GenerateTable


# level logging
logging.basicConfig(level=logging.INFO)
logging.info("____________Logging loaded____________")

# run parsing and database saving
object = GenerateTable('github')  # If you don't want save to the database
                                  # GenerateTable('github', False)
object.getMyData()

logging.info("The data is received and written to the table class and database")

w = Writer('output', datetime.now(), object.table)
w.write()

logging.info("Data has been successfully written to file")
