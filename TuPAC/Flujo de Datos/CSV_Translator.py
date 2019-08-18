#CSV

fileName = "archivo.csv"

f = open(fileName, "r")
content = f.read()
f.close()

rows = content.split("\n")
solution = []

for row in rows:
    columns = row.split(",")
    solution.append(columns)

print (solution)