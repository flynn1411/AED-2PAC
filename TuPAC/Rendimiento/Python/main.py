#-*-coding:utf-8-*-

from algorithms import (
    SelectionSort,
    InsertionSort,
    BubbleSort,
    QuickSort
)

from performance import (
    TestPerformance,
    ExecutionTime,
    ArrayGenerator
)

execution = ExecutionTime()
test = TestPerformance()
arrayGenerator = ArrayGenerator()
array = arrayGenerator.generate(10000)

bubbleSort = BubbleSort()
insertionSort = InsertionSort()
selectionSort = SelectionSort()
quickSort = QuickSort()

bubble = test.test(
    bubbleSort,
    execution, 
    array[:]
)

insertion = test.test(
    insertionSort,
    execution, 
    array[:]
)

selection = test.test(
    selectionSort,
    execution, 
    array[:]
)

quick = test.test(
    quickSort,
    execution, 
    array[:]
)

print("Algoritmo  #Datos  Tiempo(ms)")
print(bubble)
print(insertion)
print(selection)
print(quick)