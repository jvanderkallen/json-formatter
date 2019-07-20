import sys
import parser

class Object:
	def __init__(self, *members):
		self.members = members

class Member:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class Array:
	def __init__(self, *elements):
		self.elements = elements

class Literal:
	def __init__(self, value):
		self.value = value


def from_parse_tree_to_ast(node):
	if isinstance(node, parser.JsonNode):
		return from_parse_tree_to_ast(node.child)
	elif isinstance(node, parser.ObjNode):
		members = []
		for i in node.members:
			members.append(from_parse_tree_to_ast(i))
		return Object(*members)
	elif isinstance(node, parser.ArrayNode):
		elements = []
		for i in node.elements:
			elements.append(from_parse_tree_to_ast(i))
		return Array(*elements)
	elif isinstance(node, parser.ExpressionNode):
		return from_parse_tree_to_ast(node.child)
	elif isinstance(node, parser.MemberNode):
		return Member(from_parse_tree_to_ast(node.key), from_parse_tree_to_ast(node.value))
	elif isinstance(node, parser.KeyNode):
		return node.value
	elif isinstance(node, parser.ValueNode):
		return from_parse_tree_to_ast(node.expression)
	elif isinstance(node, parser.ElementNode):
		return from_parse_tree_to_ast(node.expression)
	elif isinstance(node, parser.PrimitiveNode):
		return Literal(node.value)

