#-*-coding:utf-8-*-
class Translator:
    def __init__(self, type):
        self.type = type

    def translate(self, fileName):
        solution = []
        token = " "

        f = open(fileName, "r")
        content = f.read()
        f.close()

        if (self.type is "csv"):
            token = ","

        elif (self.type is "tsv"):
            token = " "
        
        else:
            print ("E: Terminación de archivo no identificado.")

        rows = content.split("\n")
        
        for row in rows:
            column = row.split(token)
            solution.append(column)

        return solution