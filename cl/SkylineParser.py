# Generated from Skyline.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\5\5\35\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7")
        buf.write("\5(\n\5\f\5\16\5+\13\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\2\3\b\b\2\4\6\b\n\f\2\3\3\2\7\b\2\66\2\16")
        buf.write("\3\2\2\2\4\23\3\2\2\2\6\25\3\2\2\2\b\34\3\2\2\2\n,\3\2")
        buf.write("\2\2\f.\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2")
        buf.write("\2\21\24\5\6\4\2\22\24\5\b\5\2\23\21\3\2\2\2\23\22\3\2")
        buf.write("\2\2\24\5\3\2\2\2\25\26\7\7\2\2\26\27\7\3\2\2\27\30\5")
        buf.write("\b\5\2\30\7\3\2\2\2\31\35\b\5\1\2\32\35\5\f\7\2\33\35")
        buf.write("\5\n\6\2\34\31\3\2\2\2\34\32\3\2\2\2\34\33\3\2\2\2\35")
        buf.write(")\3\2\2\2\36\37\f\6\2\2\37 \7\t\2\2 (\5\b\5\7!\"\f\5\2")
        buf.write("\2\"#\7\n\2\2#(\5\b\5\6$%\f\4\2\2%&\7\13\2\2&(\5\b\5\5")
        buf.write("\'\36\3\2\2\2\'!\3\2\2\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2")
        buf.write("\2)*\3\2\2\2*\t\3\2\2\2+)\3\2\2\2,-\t\2\2\2-\13\3\2\2")
        buf.write("\2./\7\4\2\2/\60\7\b\2\2\60\61\7\5\2\2\61\62\7\b\2\2\62")
        buf.write("\63\7\5\2\2\63\64\7\b\2\2\64\65\7\6\2\2\65\r\3\2\2\2\6")
        buf.write("\23\34\')")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'('", "','", "')'", "<INVALID>", 
                     "<INVALID>", "'*'", "'+'", "'-'", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "NUM", "PER", "MES", "MENYS", 
                      "NL" ]

    RULE_root = 0
    RULE_instruccio = 1
    RULE_assig = 2
    RULE_expr = 3
    RULE_simbol = 4
    RULE_edifici = 5

    ruleNames =  [ "root", "instruccio", "assig", "expr", "simbol", "edifici" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    VAR=5
    NUM=6
    PER=7
    MES=8
    MENYS=9
    NL=10

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
            self.state = 12
            self.instruccio()
            self.state = 13
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
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 15
                self.assig()
                pass

            elif la_ == 2:
                self.state = 16
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
            self.state = 19
            self.match(SkylineParser.VAR)
            self.state = 20
            self.match(SkylineParser.T__0)
            self.state = 21
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

        def edifici(self):
            return self.getTypedRuleContext(SkylineParser.EdificiContext,0)


        def simbol(self):
            return self.getTypedRuleContext(SkylineParser.SimbolContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def PER(self):
            return self.getToken(SkylineParser.PER, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

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
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 24
                self.edifici()
                pass

            elif la_ == 3:
                self.state = 25
                self.simbol()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 29
                        self.match(SkylineParser.PER)
                        self.state = 30
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        self.match(SkylineParser.MES)
                        self.state = 33
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(SkylineParser.MENYS)
                        self.state = 36
                        self.expr(3)
                        pass

             
                self.state = 41
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==SkylineParser.VAR or _la==SkylineParser.NUM):
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
            self.state = 44
            self.match(SkylineParser.T__1)
            self.state = 45
            self.match(SkylineParser.NUM)
            self.state = 46
            self.match(SkylineParser.T__2)
            self.state = 47
            self.match(SkylineParser.NUM)
            self.state = 48
            self.match(SkylineParser.T__2)
            self.state = 49
            self.match(SkylineParser.NUM)
            self.state = 50
            self.match(SkylineParser.T__3)
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




