# Generated from Json.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\5\2\31\n\2\3\3")
        buf.write("\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\7\4%\n\4\f\4\16")
        buf.write("\4(\13\4\5\4*\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\7\b;\n\b\f\b\16\b>\13\b\5\b@")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4")
        buf.write("\6\b\n\f\16\20\22\24\2\3\4\2\b\n\f\f\2F\2\30\3\2\2\2\4")
        buf.write("\35\3\2\2\2\6\37\3\2\2\2\b-\3\2\2\2\n\61\3\2\2\2\f\63")
        buf.write("\3\2\2\2\16\65\3\2\2\2\20C\3\2\2\2\22E\3\2\2\2\24G\3\2")
        buf.write("\2\2\26\31\5\6\4\2\27\31\5\16\b\2\30\26\3\2\2\2\30\27")
        buf.write("\3\2\2\2\31\3\3\2\2\2\32\36\5\6\4\2\33\36\5\16\b\2\34")
        buf.write("\36\5\22\n\2\35\32\3\2\2\2\35\33\3\2\2\2\35\34\3\2\2\2")
        buf.write("\36\5\3\2\2\2\37)\7\3\2\2 &\5\b\5\2!\"\5\24\13\2\"#\5")
        buf.write("\b\5\2#%\3\2\2\2$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'*\3\2\2\2(&\3\2\2\2) \3\2\2\2)*\3\2\2\2*+\3\2\2")
        buf.write("\2+,\7\4\2\2,\7\3\2\2\2-.\5\n\6\2./\7\5\2\2/\60\5\f\7")
        buf.write("\2\60\t\3\2\2\2\61\62\7\t\2\2\62\13\3\2\2\2\63\64\5\4")
        buf.write("\3\2\64\r\3\2\2\2\65?\7\6\2\2\66<\5\20\t\2\678\5\24\13")
        buf.write("\289\5\20\t\29;\3\2\2\2:\67\3\2\2\2;>\3\2\2\2<:\3\2\2")
        buf.write("\2<=\3\2\2\2=@\3\2\2\2><\3\2\2\2?\66\3\2\2\2?@\3\2\2\2")
        buf.write("@A\3\2\2\2AB\7\7\2\2B\17\3\2\2\2CD\5\4\3\2D\21\3\2\2\2")
        buf.write("EF\t\2\2\2F\23\3\2\2\2GH\7\13\2\2H\25\3\2\2\2\b\30\35")
        buf.write("&)<?")
        return buf.getvalue()


class JsonParser ( Parser ):

    grammarFileName = "Json.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "':'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "STRING", "BOOLEAN", 
                      "DELIMITER", "NULL", "WS" ]

    RULE_json = 0
    RULE_expression = 1
    RULE_obj = 2
    RULE_member = 3
    RULE_key = 4
    RULE_value = 5
    RULE_array = 6
    RULE_element = 7
    RULE_primitive = 8
    RULE_delimiter = 9

    ruleNames =  [ "json", "expression", "obj", "member", "key", "value", 
                   "array", "element", "primitive", "delimiter" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    STRING=7
    BOOLEAN=8
    DELIMITER=9
    NULL=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj(self):
            return self.getTypedRuleContext(JsonParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JsonParser.ArrayContext,0)


        def getRuleIndex(self):
            return JsonParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = JsonParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JsonParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.obj()
                pass
            elif token in [JsonParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj(self):
            return self.getTypedRuleContext(JsonParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JsonParser.ArrayContext,0)


        def primitive(self):
            return self.getTypedRuleContext(JsonParser.PrimitiveContext,0)


        def getRuleIndex(self):
            return JsonParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = JsonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JsonParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.obj()
                pass
            elif token in [JsonParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.array()
                pass
            elif token in [JsonParser.NUMBER, JsonParser.STRING, JsonParser.BOOLEAN, JsonParser.NULL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.primitive()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonParser.MemberContext)
            else:
                return self.getTypedRuleContext(JsonParser.MemberContext,i)


        def delimiter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonParser.DelimiterContext)
            else:
                return self.getTypedRuleContext(JsonParser.DelimiterContext,i)


        def getRuleIndex(self):
            return JsonParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)




    def obj(self):

        localctx = JsonParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(JsonParser.T__0)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JsonParser.STRING:
                self.state = 30
                self.member()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JsonParser.DELIMITER:
                    self.state = 31
                    self.delimiter()
                    self.state = 32
                    self.member()
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 41
            self.match(JsonParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(JsonParser.KeyContext,0)


        def value(self):
            return self.getTypedRuleContext(JsonParser.ValueContext,0)


        def getRuleIndex(self):
            return JsonParser.RULE_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember" ):
                listener.enterMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember" ):
                listener.exitMember(self)




    def member(self):

        localctx = JsonParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.key()
            self.state = 44
            self.match(JsonParser.T__2)
            self.state = 45
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JsonParser.STRING, 0)

        def getRuleIndex(self):
            return JsonParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = JsonParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(JsonParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(JsonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JsonParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = JsonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonParser.ElementContext)
            else:
                return self.getTypedRuleContext(JsonParser.ElementContext,i)


        def delimiter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonParser.DelimiterContext)
            else:
                return self.getTypedRuleContext(JsonParser.DelimiterContext,i)


        def getRuleIndex(self):
            return JsonParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = JsonParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(JsonParser.T__3)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JsonParser.T__0) | (1 << JsonParser.T__3) | (1 << JsonParser.NUMBER) | (1 << JsonParser.STRING) | (1 << JsonParser.BOOLEAN) | (1 << JsonParser.NULL))) != 0):
                self.state = 52
                self.element()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JsonParser.DELIMITER:
                    self.state = 53
                    self.delimiter()
                    self.state = 54
                    self.element()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 63
            self.match(JsonParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(JsonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JsonParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = JsonParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimitiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(JsonParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(JsonParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(JsonParser.BOOLEAN, 0)

        def NULL(self):
            return self.getToken(JsonParser.NULL, 0)

        def getRuleIndex(self):
            return JsonParser.RULE_primitive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive" ):
                listener.enterPrimitive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive" ):
                listener.exitPrimitive(self)




    def primitive(self):

        localctx = JsonParser.PrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primitive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JsonParser.NUMBER) | (1 << JsonParser.STRING) | (1 << JsonParser.BOOLEAN) | (1 << JsonParser.NULL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DelimiterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELIMITER(self):
            return self.getToken(JsonParser.DELIMITER, 0)

        def getRuleIndex(self):
            return JsonParser.RULE_delimiter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelimiter" ):
                listener.enterDelimiter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelimiter" ):
                listener.exitDelimiter(self)




    def delimiter(self):

        localctx = JsonParser.DelimiterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_delimiter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(JsonParser.DELIMITER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





