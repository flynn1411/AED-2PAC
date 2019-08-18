class Node:
    """
    Arbol binario de busqueda o Binary Search Tree
    """
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def addRoot(self, value):
        self.root = Node(value)
        return True

    def _add(self, value):
        return self._addInner(value, self.root);
    
    def _addInner(self, value, current):
        #Si la raiz no existe, entonces el nuevo nodo es la raiz
        if (not self.root):
            return self.addRoot(value)

        else:
            if (value > current.value):
                if (current.rightChild):
                    current = current.rightChild
                    return self._addInner(value, current)
                
                else:
                    current.rightChild = Node(value)
                    return True
            
            else:
                if (current.leftChild):
                    current = current.leftChild
                    return self._addInner(value, current)
                
                else:
                    current.leftChild = Node(value)
                    return True
        
        return False

    def _search(self, value):
        return self._searchInner(value, self.root)

    def _searchInner(self, value, current = None):
        if (not current):
            current = self.root

        if (current.value is value):
            print(current.value)

        elif(current.value < value):
            if(current.rightChild):
                current = current.rightChild
                self._searchInner(value, current)
            
            else:
                print("%s was not found"%(value))

        else:
            if(current.leftChild):
                current = current.leftChild
                self._searchInner(value, current)
            else:
                print("%s was not found"%(value))

    def _traverse(self):
        self._traverseInner(self.root)

    def _traverseInner(self, current):
        if (current.leftChild):
            self._traverseInner(current.leftChild)

        print(current.value)
        
        if (current.rightChild):
            self._traverseInner(current.rightChild)
