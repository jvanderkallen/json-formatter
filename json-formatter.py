import sys
from antlr4 import *
from JsonLexer import JsonLexer
from JsonParser import JsonParser
from JsonListener import JsonListener

class EmptyContext():
    def is_array(self):
        return False

    def is_object(self):
        return False

class ArrayContext():
    def is_array(self):
        return True

    def is_object(self):
        return False

class ObjectContext():
    def is_array(self):
        return False

    def is_object(self):
        return True

class CurrentContext:
    def __init__(self):
        self.contexts = [EmptyContext()]
        self.indentation_level = 0

    def is_object(self):
        return self.last_context().is_object()

    def is_array(self):
        return self.last_context().is_array()

    def last_context(self):
        return self.contexts[len(self.contexts) - 1]

    def enter_array(self):
        self.contexts.append(ArrayContext())

    def enter_object(self):
        self.contexts.append(ObjectContext())

    def exit_context(self):
        self.contexts.pop()

    def increment_indentation_level(self):
        self.indentation_level += 1

    def decrement_indentation_level(self):
        self.indentation_level -= 1

class JsonFormatterListener(JsonListener):
    def __init__(self, spaces_per_level):
        self.current_context = CurrentContext()
        self.SPACES_PER_LEVEL = spaces_per_level

    def print_indentation(self):
        for level in range(self.current_context.indentation_level):
            for i in range(self.SPACES_PER_LEVEL):
                sys.stdout.write(' ')

    def print_member_key(self, key):
        self.print_indentation()
        sys.stdout.write(key + ': ')                

    def enterObj(self, ctx:JsonParser.ObjContext):
        if self.current_context.is_array():
            self.print_indentation()

        self.current_context.enter_object()

        print('{')
        self.current_context.increment_indentation_level()

    def exitObj(self, ctx:JsonParser.ObjContext):
        self.current_context.decrement_indentation_level()
        self.print_indentation()
        sys.stdout.write('}')
        self.current_context.exit_context()

    def enterArray(self, ctx:JsonParser.ArrayContext):
        self.current_context.enter_array()
        print('[')
        self.current_context.increment_indentation_level()

    def exitArray(self, ctx:JsonParser.ArrayContext):
        self.current_context.decrement_indentation_level()
        self.print_indentation()
        sys.stdout.write(']')
        self.current_context.exit_context()        

    def enterMember(self, ctx:JsonParser.MemberContext):
        self.print_member_key(ctx.key().getText())

    def enterLastMember(self, ctx:JsonParser.LastMemberContext):
        self.print_member_key(ctx.key().getText())

    def exitMember(self, ctx:JsonParser.MemberContext):
        print(',')

    def exitLastMember(self, ctx:JsonParser.LastMemberContext):
        print('')

    def exitElement(self, ctx:JsonParser.ElementContext):
        print(',')

    def exitLastElement(self, ctx:JsonParser.LastElementContext):
        print('')

    def enterPrimitive(self, ctx:JsonParser.PrimitiveContext):
        if self.current_context.is_array():
            self.print_indentation()

        sys.stdout.write(ctx.getText())

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JsonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JsonParser(stream)
    tree = parser.json()

    walker = ParseTreeWalker()
    walker.walk(JsonFormatterListener(4), tree)
 
if __name__ == '__main__':
    main(sys.argv)