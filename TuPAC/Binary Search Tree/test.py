from bst import*

tree = BinarySearchTree()
tree._add(10)
tree._add(1)
tree._add(4)
tree._add(13)
tree._add(28)
tree._add(2)

tree._search(1)
tree._search(28)
tree._search(3)
print("\n")

tree._traverse()