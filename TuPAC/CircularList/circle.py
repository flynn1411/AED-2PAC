"""
Lista Circular: El último nodo de la lista apunta al primero de la lista
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularList:
    def __init__(self):
        self.first = None

    def _add(self, value):
        if (not self.first):
            self.first = Node(value)
            self.first.next = self.first

        else:
            current = self.first
            while(current.next is not self.first):
                current = current.next

            current.next = Node(value)
            current.next.next = self.first
            
    def _print(self, current = None):
        #Para comenzar la recursión
        if (not current):
            current = self.first

        #Decisión de la recursión
        if (current.next is not self.first):
            print(current.value)
            current = current.next
            self._print(current)

        else:
            print("None")

            

list = CircularList()
list._add(1)
list._add(2)
list._add(3)
list._add("Cuarto")
list._add(6)
list._print()
