from datetime import datetime
import random

class TestPerformance:
    def __init__(self):
        pass

    def test(self, algorithm, execution, array):
        initTime = execution.getTime()
        algorithm.sort(array)
        finalTime = execution.getTime()

        return (algorithm.name, len(array), execution.diff(initTime, finalTime))

class ExecutionTime:
    def __init__(self):
        pass

    def getTime(self):
        return datetime.now()

    def diff(self, i, f):
        r = f-i
        milliseconds = r.days*24*60*60*1000
        milliseconds += r.seconds*1000
        milliseconds += r.microseconds/100

        return milliseconds

class ArrayGenerator:
    def __init__(self):
        pass

    def generate(self, n = 100):
        array = [ int(random.random()*n) for i in range(n) ]

        return array[:]