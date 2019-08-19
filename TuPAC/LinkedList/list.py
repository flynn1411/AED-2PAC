#Nodo
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

#Lista
class LinkedList:
	def __init__(self):
		self.first = None

	def _add(self, value):

		if(not self.first):
			self.first = Node(value)
			return True

		else:
			current = self.first

			while (current.next):
				current = current.next

			current.next = Node(value)
			return True

		return False

	def _print(self, current = None, trail = " "):
		if (not current):
			current = self.first

		if (current.next):
			trail = ("%s %s ->" %(trail, current.value))
			self._print(current.next, trail)

		else:
			trail = ("%s %s" %(trail, current.value))
			print (trail)

list = LinkedList()

list._add(1)
list._add(2)
list._add(3)
list._print()