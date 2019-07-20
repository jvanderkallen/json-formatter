class JsonNode:
    def __init__(self, child):
        self.child = child

class ObjNode:
    def __init__(self, members):
        self.members = members

class ArrayNode:
    def __init__(self, elements):
        self.elements = elements

class ExpressionNode:
    def __init__(self, child):
        self.child = child

class MemberNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class KeyNode:
    def __init__(self, value):
        self.value = value

class ValueNode:
    def __init__(self, expression):
        self.expression = expression

class ElementNode:
    def __init__(self, expression):
        self.expression = expression

class PrimitiveNode:
    def __init__(self, value):
        self.value = value

class ParseException(BaseException):
    def __init__(self, position):
        self.position = position

class JsonParser:
    def __init__(self, tokens):
        self.tokens = tokens

    def current_token(self):
        return self.tokens[self.current_position]

    def go_to_next_token(self):
        self.current_position += 1

    def current_token_is_of_type(self, *types):
        for token_type in types:
            if self.current_token().token_type == token_type:
                return True
        return False

    def parse(self):
        self.current_position = 0
        return self.json()      

    def json(self):
        if self.current_token_is_of_type('OBJECT_OPEN'):
            return JsonNode(self.obj())
        elif self.current_token_is_of_type('ARRAY_OPEN'):
            return JsonNode(self.array())
        raise ParseException(self.current_position)

    def obj(self):
        self.go_to_next_token()
        members = []
        first = True
        while True:
            if first and self.current_token_is_of_type('STRING'):
                members.append(self.member())
                first = False
            elif not first and self.current_token_is_of_type('DELIMITER'):
                self.go_to_next_token()
                if self.current_token_is_of_type('STRING'):
                    members.append(self.member())
            elif self.current_token_is_of_type('OBJECT_CLOSE'):
                self.go_to_next_token()
                break
            else:
                raise ParseException(self.current_position)

        return ObjNode(members)

    def array(self):
        self.go_to_next_token()
        elements = []
        first = True
        while True:
            if first and self.current_token_is_of_type('OBJECT_OPEN', 'ARRAY_OPEN', 'NUMBER', 'STRING', 'BOOLEAN', 'NULL'):
                elements.append(self.element())
                first = False
            elif not first and self.current_token_is_of_type('DELIMITER'):
                self.go_to_next_token()
                if self.current_token_is_of_type('OBJECT_OPEN', 'ARRAY_OPEN', 'NUMBER', 'STRING', 'BOOLEAN', 'NULL'):
                    elements.append(self.element())
            elif self.current_token_is_of_type('ARRAY_CLOSE'):
                self.go_to_next_token()
                break
            else:
                raise ParseException(self.current_position)

        return ArrayNode(elements)

    def expression(self):
        if self.current_token_is_of_type('OBJECT_OPEN'):
            return ExpressionNode(self.obj())
        elif self.current_token_is_of_type('ARRAY_OPEN'):
            return ExpressionNode(self.array())
        elif self.current_token_is_of_type('NUMBER', 'STRING', 'BOOLEAN', 'NULL'):
            return ExpressionNode(self.primitive())
        raise ParseException(self.current_position)

    def member(self):
        if self.current_token_is_of_type('STRING'):
            key = self.key()
            if self.current_token_is_of_type('COLON'):
                self.go_to_next_token()
                if self.current_token_is_of_type('OBJECT_OPEN', 'ARRAY_OPEN', 'NUMBER', 'STRING', 'BOOLEAN', 'NULL'):
                    return MemberNode(key, self.expression())
        raise ParseException(self.current_position)

    def key(self):
        res = KeyNode(self.current_token().lexeme)
        self.go_to_next_token()
        return res

    def value(self):
        return ValueNode(self.expression())

    def element(self):
        return ElementNode(self.expression())

    def primitive(self):
        res = PrimitiveNode(self.current_token().lexeme)
        self.go_to_next_token()
        return res
