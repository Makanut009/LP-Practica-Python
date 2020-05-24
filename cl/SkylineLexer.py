# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\6\5\36\n\5\r\5\16\5\37\3\6\6\6#\n\6\r\6\16\6$\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\6\n.\n\n\r\n\16\n/\3\n\3\n\2")
        buf.write("\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\5\3")
        buf.write("\2c|\3\2\62;\4\2\f\f\"\"\2\65\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\30\3")
        buf.write("\2\2\2\7\32\3\2\2\2\t\35\3\2\2\2\13\"\3\2\2\2\r&\3\2\2")
        buf.write("\2\17(\3\2\2\2\21*\3\2\2\2\23-\3\2\2\2\25\26\7<\2\2\26")
        buf.write("\27\7?\2\2\27\4\3\2\2\2\30\31\7*\2\2\31\6\3\2\2\2\32\33")
        buf.write("\7+\2\2\33\b\3\2\2\2\34\36\t\2\2\2\35\34\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \n\3\2\2\2!#\t\3\2")
        buf.write("\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\f\3\2\2")
        buf.write("\2&\'\7,\2\2\'\16\3\2\2\2()\7-\2\2)\20\3\2\2\2*+\7/\2")
        buf.write("\2+\22\3\2\2\2,.\t\4\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2")
        buf.write("/\60\3\2\2\2\60\61\3\2\2\2\61\62\b\n\2\2\62\24\3\2\2\2")
        buf.write("\6\2\37$/\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    VAR = 4
    NUM = 5
    PER = 6
    MES = 7
    MENYS = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "')'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "NUM", "PER", "MES", "MENYS", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "VAR", "NUM", "PER", "MES", "MENYS", 
                  "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


