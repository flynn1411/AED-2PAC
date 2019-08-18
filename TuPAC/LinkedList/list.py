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

	def _print(self, current = None):
		if (not current):
			current = self.first

		if (current.next):
			print (current.value)
			current = current.next
			self._print(current)

		else:
			print (current.value)

list = LinkedList()

list._add(1)
list._add(2)
list._add(3)
list._print()