# Generated from Skyline.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\5\3\30\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5(\n")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\63\n\5\f\5")
        buf.write("\16\5\66\13\5\3\6\3\6\3\6\5\6;\n\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\bI\n\b\f\b\16\bL\13\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\2\3\b\n\2\4\6\b\n\f\16\20\2\2\2^\2\22\3\2\2\2\4\27")
        buf.write("\3\2\2\2\6\31\3\2\2\2\b\'\3\2\2\2\n:\3\2\2\2\f<\3\2\2")
        buf.write("\2\16D\3\2\2\2\20O\3\2\2\2\22\23\5\4\3\2\23\24\7\2\2\3")
        buf.write("\24\3\3\2\2\2\25\30\5\6\4\2\26\30\5\b\5\2\27\25\3\2\2")
        buf.write("\2\27\26\3\2\2\2\30\5\3\2\2\2\31\32\7\13\2\2\32\33\7\3")
        buf.write("\2\2\33\34\5\b\5\2\34\7\3\2\2\2\35\36\b\5\1\2\36(\5\n")
        buf.write("\6\2\37(\5\16\b\2 (\5\20\t\2!\"\7\t\2\2\"#\5\b\5\2#$\7")
        buf.write("\n\2\2$(\3\2\2\2%&\7\17\2\2&(\5\n\6\2\'\35\3\2\2\2\'\37")
        buf.write("\3\2\2\2\' \3\2\2\2\'!\3\2\2\2\'%\3\2\2\2(\64\3\2\2\2")
        buf.write(")*\f\7\2\2*+\7\r\2\2+\63\5\b\5\b,-\f\6\2\2-.\7\16\2\2")
        buf.write(".\63\5\b\5\7/\60\f\5\2\2\60\61\7\17\2\2\61\63\5\b\5\6")
        buf.write("\62)\3\2\2\2\62,\3\2\2\2\62/\3\2\2\2\63\66\3\2\2\2\64")
        buf.write("\62\3\2\2\2\64\65\3\2\2\2\65\t\3\2\2\2\66\64\3\2\2\2\67")
        buf.write(";\5\f\7\28;\7\13\2\29;\7\f\2\2:\67\3\2\2\2:8\3\2\2\2:")
        buf.write("9\3\2\2\2;\13\3\2\2\2<=\7\t\2\2=>\7\f\2\2>?\7\4\2\2?@")
        buf.write("\7\f\2\2@A\7\4\2\2AB\7\f\2\2BC\7\n\2\2C\r\3\2\2\2DE\7")
        buf.write("\5\2\2EJ\5\f\7\2FG\7\4\2\2GI\5\f\7\2HF\3\2\2\2IL\3\2\2")
        buf.write("\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2LJ\3\2\2\2MN\7\6\2\2N")
        buf.write("\17\3\2\2\2OP\7\7\2\2PQ\7\f\2\2QR\7\4\2\2RS\7\f\2\2ST")
        buf.write("\7\4\2\2TU\7\f\2\2UV\7\4\2\2VW\7\f\2\2WX\7\4\2\2XY\7\f")
        buf.write("\2\2YZ\7\b\2\2Z\21\3\2\2\2\b\27\'\62\64:J")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "','", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "'*'", "'+'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", 
                      "VAR", "NUM", "PER", "MES", "MENYS", "WS" ]

    RULE_root = 0
    RULE_instruccio = 1
    RULE_assig = 2
    RULE_expr = 3
    RULE_simbol = 4
    RULE_edifici = 5
    RULE_compost = 6
    RULE_random = 7

    ruleNames =  [ "root", "instruccio", "assig", "expr", "simbol", "edifici", 
                   "compost", "random" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    LPAREN=7
    RPAREN=8
    VAR=9
    NUM=10
    PER=11
    MES=12
    MENYS=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccio(self):
            return self.getTypedRuleContext(SkylineParser.InstruccioContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.instruccio()
            self.state = 17
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstruccioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assig(self):
            return self.getTypedRuleContext(SkylineParser.AssigContext,0)


        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_instruccio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccio" ):
                return visitor.visitInstruccio(self)
            else:
                return visitor.visitChildren(self)




    def instruccio(self):

        localctx = SkylineParser.InstruccioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 19
                self.assig()
                pass

            elif la_ == 2:
                self.state = 20
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SkylineParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = SkylineParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(SkylineParser.VAR)
            self.state = 24
            self.match(SkylineParser.T__0)
            self.state = 25
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simbol(self):
            return self.getTypedRuleContext(SkylineParser.SimbolContext,0)


        def compost(self):
            return self.getTypedRuleContext(SkylineParser.CompostContext,0)


        def random(self):
            return self.getTypedRuleContext(SkylineParser.RandomContext,0)


        def LPAREN(self):
            return self.getToken(SkylineParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(SkylineParser.RPAREN, 0)

        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

        def PER(self):
            return self.getToken(SkylineParser.PER, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 28
                self.simbol()
                pass

            elif la_ == 2:
                self.state = 29
                self.compost()
                pass

            elif la_ == 3:
                self.state = 30
                self.random()
                pass

            elif la_ == 4:
                self.state = 31
                self.match(SkylineParser.LPAREN)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(SkylineParser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 35
                self.match(SkylineParser.MENYS)
                self.state = 36
                self.simbol()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 40
                        self.match(SkylineParser.PER)
                        self.state = 41
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 43
                        self.match(SkylineParser.MES)
                        self.state = 44
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 46
                        self.match(SkylineParser.MENYS)
                        self.state = 47
                        self.expr(4)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SimbolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edifici(self):
            return self.getTypedRuleContext(SkylineParser.EdificiContext,0)


        def VAR(self):
            return self.getToken(SkylineParser.VAR, 0)

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_simbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimbol" ):
                return visitor.visitSimbol(self)
            else:
                return visitor.visitChildren(self)




    def simbol(self):

        localctx = SkylineParser.SimbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simbol)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.edifici()
                pass
            elif token in [SkylineParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(SkylineParser.VAR)
                pass
            elif token in [SkylineParser.NUM]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(SkylineParser.NUM)
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

    class EdificiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_edifici

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdifici" ):
                return visitor.visitEdifici(self)
            else:
                return visitor.visitChildren(self)




    def edifici(self):

        localctx = SkylineParser.EdificiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_edifici)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(SkylineParser.LPAREN)
            self.state = 59
            self.match(SkylineParser.NUM)
            self.state = 60
            self.match(SkylineParser.T__1)
            self.state = 61
            self.match(SkylineParser.NUM)
            self.state = 62
            self.match(SkylineParser.T__1)
            self.state = 63
            self.match(SkylineParser.NUM)
            self.state = 64
            self.match(SkylineParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edifici(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.EdificiContext)
            else:
                return self.getTypedRuleContext(SkylineParser.EdificiContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_compost

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompost" ):
                return visitor.visitCompost(self)
            else:
                return visitor.visitChildren(self)




    def compost(self):

        localctx = SkylineParser.CompostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compost)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(SkylineParser.T__2)
            self.state = 67
            self.edifici()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__1:
                self.state = 68
                self.match(SkylineParser.T__1)
                self.state = 69
                self.edifici()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(SkylineParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RandomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_random

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom" ):
                return visitor.visitRandom(self)
            else:
                return visitor.visitChildren(self)




    def random(self):

        localctx = SkylineParser.RandomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_random)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SkylineParser.T__4)
            self.state = 78
            self.match(SkylineParser.NUM)
            self.state = 79
            self.match(SkylineParser.T__1)
            self.state = 80
            self.match(SkylineParser.NUM)
            self.state = 81
            self.match(SkylineParser.T__1)
            self.state = 82
            self.match(SkylineParser.NUM)
            self.state = 83
            self.match(SkylineParser.T__1)
            self.state = 84
            self.match(SkylineParser.NUM)
            self.state = 85
            self.match(SkylineParser.T__1)
            self.state = 86
            self.match(SkylineParser.NUM)
            self.state = 87
            self.match(SkylineParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




