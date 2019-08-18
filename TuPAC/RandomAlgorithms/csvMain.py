from randomCSV import *

csvInstance = CSV()

content = csvInstance.generateCSV()

f = open("archivo.csv", "w")
f.write(content)
f.close()