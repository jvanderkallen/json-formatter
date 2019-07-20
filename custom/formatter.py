import sys
import ast

class JsonFormatter:
	def __init__(self, root):
		self.root = root

	def print_indentation(self):
		for i in range(self.level):
			sys.stdout.write('    ')

	def print_indented(self, str):
		self.print_indentation()
		sys.stdout.write(str)

	def traverse(self, node):
		if isinstance(node, ast.Object):
			print('{')
			self.level += 1

			number_of_members = len(node.members)
			for index, node in enumerate(node.members):
				self.print_indented(node.key + ': ')
				if isinstance(node.value, ast.Literal):
					sys.stdout.write(node.value.value)
				else:
					self.traverse(node.value)

				if index < number_of_members - 1:
					print(',')
				else:
					print('')	

			self.level -= 1
			self.print_indented('}')
		elif isinstance(node, ast.Array):
			print('[')
			self.level += 1

			number_of_elements = len(node.elements)
			for index, element in enumerate(node.elements):
				if isinstance(element, ast.Literal):
					self.print_indented(element.value)
				else:
					self.print_indentation()
					self.traverse(element)

				if index < number_of_elements - 1:
					print(',')
				else:
					print('')

			self.level -= 1
			self.print_indented(']')


	def print_formatted(self):
		self.level = 0
		self.traverse(self.root)
