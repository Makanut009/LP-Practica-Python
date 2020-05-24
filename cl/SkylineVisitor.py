# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    def __init__(self):
        self.taula_simbols = {}

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        print("miau")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#instruccio.
    def visitInstruccio(self, ctx:SkylineParser.InstruccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        self.taula_simbols[ctx.VAR().getText()] = self.visit(ctx.expr())


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.simbol())
        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]
            if l[1].getSymbol().type == SkylineParser.PER:
                return self.visit(l[0]) * self.visit(l[2])
            elif l[1].getSymbol().type == SkylineParser.MES:
                return self.visit(l[0]) + self.visit(l[2])
            elif l[1].getSymbol().type == SkylineParser.MENYS:
                return self.visit(l[0]) - self.visit(l[2])


    # Visit a parse tree produced by SkylineParser#simbol.
    def visitSimbol(self, ctx:SkylineParser.SimbolContext):
        isVar = ctx.VAR() is not None
        return self.taula_simbols[ctx.getText()] if isVar else int(ctx.getText())


del SkylineParser