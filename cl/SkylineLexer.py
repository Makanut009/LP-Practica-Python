# Generated from Skyline.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\7\n\63\n\n\f\n")
        buf.write("\16\n\66\13\n\3\13\5\139\n\13\3\13\6\13<\n\13\r\13\16")
        buf.write("\13=\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17G\n\17\r\17\16")
        buf.write("\17H\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\6\3\2c|\4\2\62")
        buf.write(";c|\3\2\62;\5\2\13\f\17\17\"\"\2O\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37")
        buf.write("\3\2\2\2\5\"\3\2\2\2\7$\3\2\2\2\t&\3\2\2\2\13(\3\2\2\2")
        buf.write("\r*\3\2\2\2\17,\3\2\2\2\21.\3\2\2\2\23\60\3\2\2\2\258")
        buf.write("\3\2\2\2\27?\3\2\2\2\31A\3\2\2\2\33C\3\2\2\2\35F\3\2\2")
        buf.write("\2\37 \7<\2\2 !\7?\2\2!\4\3\2\2\2\"#\7.\2\2#\6\3\2\2\2")
        buf.write("$%\7]\2\2%\b\3\2\2\2&\'\7_\2\2\'\n\3\2\2\2()\7}\2\2)\f")
        buf.write("\3\2\2\2*+\7\177\2\2+\16\3\2\2\2,-\7*\2\2-\20\3\2\2\2")
        buf.write("./\7+\2\2/\22\3\2\2\2\60\64\t\2\2\2\61\63\t\3\2\2\62\61")
        buf.write("\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\24\3\2\2\2\66\64\3\2\2\2\679\7/\2\28\67\3\2\2\289\3\2")
        buf.write("\2\29;\3\2\2\2:<\t\4\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2")
        buf.write("=>\3\2\2\2>\26\3\2\2\2?@\7,\2\2@\30\3\2\2\2AB\7-\2\2B")
        buf.write("\32\3\2\2\2CD\7/\2\2D\34\3\2\2\2EG\t\5\2\2FE\3\2\2\2G")
        buf.write("H\3\2\2\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\17\2\2K\36")
        buf.write("\3\2\2\2\b\2\62\648=H\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    PARES = 7
    PARDR = 8
    VAR = 9
    NUM = 10
    PER = 11
    MES = 12
    MENYS = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "','", "'['", "']'", "'{'", "'}'", "'('", "')'", "'*'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "PARES", "PARDR", "VAR", "NUM", "PER", "MES", "MENYS", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "PARES", 
                  "PARDR", "VAR", "NUM", "PER", "MES", "MENYS", "WS" ]

    grammarFileName = "Skyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


