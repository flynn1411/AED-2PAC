class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.children = LinkedList()

class LinkedList:
    def __init__(self):
        self.first = None

    def addToList(self, value):
        if(not self.first):
            self.first = Node(value)

        else:
            current = self.first

            while(current.next):
                current = current.next

            current.next = Node(value)

    def printList(self, current = None, trail = "->"):
        if(not current):
            current = self.first

        if(current.next):
            trail = ("%s%s -> " %(trail, current.value))
            current = current.next
            self.printList(current, trail)

        else:
            trail = ("%s%s -> NULL" %(trail, current.value))
            print(trail)

    def searchInList(self, value, current = None):
        if (not current):
            current = self.first

        if(current.next):
            if(current.value is value):
                return True
            
            else:
                current = current.next
                return self.searchInList(value, current)

        else:
            if(current.value is value):
                return True
            else:
                return False

"""list = LinkedList()

list.addToList("2")
list.addToList(3)
list.addToList("Hola Mundo")
list.addToList("Nodo")
list.addToList(2.5)

print(list.searchInList(8))
print(list.searchInList(3))

list.printList()"""