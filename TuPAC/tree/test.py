from tree import*

def printSearchFunction(nodeWasFound):
    if (nodeWasFound):
        print (True)
    
    else:
        print (False)

tree = Tree()

tree._add(3)
tree._add("H")
tree._add("A.py")
tree._add(40, "AED")

tree._add(8, "H")
tree._add(10, "A.py")
tree._add("Hola", "A.py")

foundNode0 = tree._search(10)
foundNode1 = tree._search(8)
foundNode2 = tree._search("Adios")

printSearchFunction(foundNode0)
printSearchFunction(foundNode1)
printSearchFunction(foundNode2)