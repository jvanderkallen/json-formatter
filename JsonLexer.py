# Generated from Json.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\5\7%\n\7\3\7\6\7(\n\7")
        buf.write("\r\7\16\7)\3\7\3\7\6\7.\n\7\r\7\16\7/\5\7\62\n\7\3\b\3")
        buf.write("\b\3\b\3\b\7\b8\n\b\f\b\16\b;\13\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\5\tH\n\t\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\6\fR\n\f\r\f\16\fS\3\f\3\f\2\2\r\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\6")
        buf.write("\3\2\62;\5\2\60\60GGgg\5\2\f\f\17\17$$\5\2\13\f\17\17")
        buf.write("\"\"\2^\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5")
        buf.write("\33\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r$\3")
        buf.write("\2\2\2\17\63\3\2\2\2\21G\3\2\2\2\23I\3\2\2\2\25K\3\2\2")
        buf.write("\2\27Q\3\2\2\2\31\32\7}\2\2\32\4\3\2\2\2\33\34\7\177\2")
        buf.write("\2\34\6\3\2\2\2\35\36\7<\2\2\36\b\3\2\2\2\37 \7]\2\2 ")
        buf.write("\n\3\2\2\2!\"\7_\2\2\"\f\3\2\2\2#%\7/\2\2$#\3\2\2\2$%")
        buf.write("\3\2\2\2%\'\3\2\2\2&(\t\2\2\2\'&\3\2\2\2()\3\2\2\2)\'")
        buf.write("\3\2\2\2)*\3\2\2\2*\61\3\2\2\2+-\t\3\2\2,.\t\2\2\2-,\3")
        buf.write("\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61")
        buf.write("+\3\2\2\2\61\62\3\2\2\2\62\16\3\2\2\2\639\7$\2\2\648\n")
        buf.write("\4\2\2\65\66\7^\2\2\668\7$\2\2\67\64\3\2\2\2\67\65\3\2")
        buf.write("\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2\2")
        buf.write("\2<=\7$\2\2=\20\3\2\2\2>?\7v\2\2?@\7t\2\2@A\7w\2\2AH\7")
        buf.write("g\2\2BC\7h\2\2CD\7c\2\2DE\7n\2\2EF\7u\2\2FH\7g\2\2G>\3")
        buf.write("\2\2\2GB\3\2\2\2H\22\3\2\2\2IJ\7.\2\2J\24\3\2\2\2KL\7")
        buf.write("p\2\2LM\7w\2\2MN\7n\2\2NO\7n\2\2O\26\3\2\2\2PR\t\5\2\2")
        buf.write("QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\b")
        buf.write("\f\2\2V\30\3\2\2\2\13\2$)/\61\679GS\3\b\2\2")
        return buf.getvalue()


class JsonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUMBER = 6
    STRING = 7
    BOOLEAN = 8
    DELIMITER = 9
    NULL = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "':'", "'['", "']'", "','", "'null'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "STRING", "BOOLEAN", "DELIMITER", "NULL", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "STRING", 
                  "BOOLEAN", "DELIMITER", "NULL", "WS" ]

    grammarFileName = "Json.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


