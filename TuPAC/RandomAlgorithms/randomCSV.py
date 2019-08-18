# -*- coding: utf-8 -*-
import random

class CSV:
    def __init__(self):
        pass

    def random2int(self, min = 0, max = 100):
        r = random.random()
        return int(r*(max-min)+min)

    def generateCSV(self):
        r = self.random2int(1, 10)
        rows = []
        for i in range(r):
            columns = []
            c = self.random2int();

            for j in range(c):
                columns.append(self.random2int())

            rows.append(",".join(str(columns)))

        content = "\n\n\n".join(rows)

        return content