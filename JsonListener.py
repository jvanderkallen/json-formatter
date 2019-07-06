# Generated from Json.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JsonParser import JsonParser
else:
    from JsonParser import JsonParser

# This class defines a complete listener for a parse tree produced by JsonParser.
class JsonListener(ParseTreeListener):

    # Enter a parse tree produced by JsonParser#json.
    def enterJson(self, ctx:JsonParser.JsonContext):
        pass

    # Exit a parse tree produced by JsonParser#json.
    def exitJson(self, ctx:JsonParser.JsonContext):
        pass


    # Enter a parse tree produced by JsonParser#expression.
    def enterExpression(self, ctx:JsonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JsonParser#expression.
    def exitExpression(self, ctx:JsonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JsonParser#obj.
    def enterObj(self, ctx:JsonParser.ObjContext):
        pass

    # Exit a parse tree produced by JsonParser#obj.
    def exitObj(self, ctx:JsonParser.ObjContext):
        pass


    # Enter a parse tree produced by JsonParser#member.
    def enterMember(self, ctx:JsonParser.MemberContext):
        pass

    # Exit a parse tree produced by JsonParser#member.
    def exitMember(self, ctx:JsonParser.MemberContext):
        pass


    # Enter a parse tree produced by JsonParser#lastMember.
    def enterLastMember(self, ctx:JsonParser.LastMemberContext):
        pass

    # Exit a parse tree produced by JsonParser#lastMember.
    def exitLastMember(self, ctx:JsonParser.LastMemberContext):
        pass


    # Enter a parse tree produced by JsonParser#key.
    def enterKey(self, ctx:JsonParser.KeyContext):
        pass

    # Exit a parse tree produced by JsonParser#key.
    def exitKey(self, ctx:JsonParser.KeyContext):
        pass


    # Enter a parse tree produced by JsonParser#value.
    def enterValue(self, ctx:JsonParser.ValueContext):
        pass

    # Exit a parse tree produced by JsonParser#value.
    def exitValue(self, ctx:JsonParser.ValueContext):
        pass


    # Enter a parse tree produced by JsonParser#array.
    def enterArray(self, ctx:JsonParser.ArrayContext):
        pass

    # Exit a parse tree produced by JsonParser#array.
    def exitArray(self, ctx:JsonParser.ArrayContext):
        pass


    # Enter a parse tree produced by JsonParser#element.
    def enterElement(self, ctx:JsonParser.ElementContext):
        pass

    # Exit a parse tree produced by JsonParser#element.
    def exitElement(self, ctx:JsonParser.ElementContext):
        pass


    # Enter a parse tree produced by JsonParser#lastElement.
    def enterLastElement(self, ctx:JsonParser.LastElementContext):
        pass

    # Exit a parse tree produced by JsonParser#lastElement.
    def exitLastElement(self, ctx:JsonParser.LastElementContext):
        pass


    # Enter a parse tree produced by JsonParser#primitive.
    def enterPrimitive(self, ctx:JsonParser.PrimitiveContext):
        pass

    # Exit a parse tree produced by JsonParser#primitive.
    def exitPrimitive(self, ctx:JsonParser.PrimitiveContext):
        pass


