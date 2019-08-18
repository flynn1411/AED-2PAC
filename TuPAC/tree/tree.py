from list import*

"""
Arbol en el cual cada nodo tiene hijos los cuales son una lista enlazada
"""

class Tree:
    def __init__(self):
        self.root = Node("/")

    def _add(self, value, referenceNode = None):
        if(not referenceNode or not self._search(referenceNode)):
            parentNode = self.root
            parentNode.children.addToList(value)
            if (not referenceNode):
                print("El nodo '%s' fue agregado en la raiz" %(value))

            else:
                print("Nodo '%s' no fue encontrado, se agregara el nodo '%s' en la raiz." %(referenceNode, value))
        
        else:
            parent = self._search(referenceNode)
            parent.children.addToList(value)
            print("El nodo '%s' fue agregado con exito como hijo del nodo '%s'." %(value, parent.value))


    def _search(self, value, current = None):
        if (not current):
            current = self.root

        if (current.next):
            if(current.value is value):
                return current
            
            else:
                if (current.children.first):
                    if (self._search(value, current.children.first)):
                        current = current.children.first
                        return self._search(value, current)
                    
                    else:
                        current = current.next
                        return self._search(value, current)

                else:
                    current = current.next
                    return self._search(value, current)

        else:
            if(current.value is value):
                return current

            else:
                if (current.children.first):
                    if (self._search(value, current.children.first)):
                        current = current.children.first
                        return self._search(value, current)
                    
                    else:
                        return None

                else:
                    return None