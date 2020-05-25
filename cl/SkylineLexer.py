# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("\67\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\6\6\"\n\6\r\6\16\6#\3\7\6\7\'\n")
        buf.write("\7\r\7\16\7(\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\62\n\13")
        buf.write("\r\13\16\13\63\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\3\2\5\3\2c|\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\29\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\32\3\2\2\2")
        buf.write("\7\34\3\2\2\2\t\36\3\2\2\2\13!\3\2\2\2\r&\3\2\2\2\17*")
        buf.write("\3\2\2\2\21,\3\2\2\2\23.\3\2\2\2\25\61\3\2\2\2\27\30\7")
        buf.write("<\2\2\30\31\7?\2\2\31\4\3\2\2\2\32\33\7.\2\2\33\6\3\2")
        buf.write("\2\2\34\35\7*\2\2\35\b\3\2\2\2\36\37\7+\2\2\37\n\3\2\2")
        buf.write("\2 \"\t\2\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2")
        buf.write("$\f\3\2\2\2%\'\t\3\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2")
        buf.write("()\3\2\2\2)\16\3\2\2\2*+\7,\2\2+\20\3\2\2\2,-\7-\2\2-")
        buf.write("\22\3\2\2\2./\7/\2\2/\24\3\2\2\2\60\62\t\4\2\2\61\60\3")
        buf.write("\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\66\b\13\2\2\66\26\3\2\2\2\6\2#(\63\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    LPAREN = 3
    RPAREN = 4
    VAR = 5
    NUM = 6
    PER = 7
    MES = 8
    MENYS = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "','", "'('", "')'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "VAR", "NUM", "PER", "MES", "MENYS", "WS" ]

    ruleNames = [ "T__0", "T__1", "LPAREN", "RPAREN", "VAR", "NUM", "PER", 
                  "MES", "MENYS", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


