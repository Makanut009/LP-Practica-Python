from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

from skyline import Skyline

class EvalVisitor(ParseTreeVisitor):

    def __init__(self):
        self.taula_simbols = {}

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#instruccio.
    def visitInstruccio(self, ctx:SkylineParser.InstruccioContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        self.taula_simbols[ctx.VAR().getText()] = self.visit(ctx.expr())

    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        print(ctx.getChildCount())
        if ctx.getChildCount() == 1:
            if next(ctx.getChildren()) == ctx.edifici():
                return self.visit(ctx.edifici())
            else:
                return self.visit(ctx.simbol())

        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]

            if l[1].getSymbol().type == SkylineParser.PER:
                sk = self.visit(l[0]) * self.visit(l[2])
                sk.mostra()
                return sk

            elif l[1].getSymbol().type == SkylineParser.MES:
                sk = self.visit(l[0]) + self.visit(l[2])
                print("Hola")
                sk.mostra()
                return sk

            elif l[1].getSymbol().type == SkylineParser.MENYS:
                sk = self.visit(l[0]) - self.visit(l[2])
                sk.mostra()
                return sk

    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        g = ctx.getChildren()
        l = [next(g).getText() for i in range(ctx.getChildCount())]
        return Skyline(int(l[1]), int(l[3]), int(l[5]))

    # Visit a parse tree produced by SkylineParser#simbol.
    def visitSimbol(self, ctx:SkylineParser.SimbolContext):
        isVar = ctx.VAR() is not None
        return self.taula_simbols[ctx.getText()] if isVar else int(ctx.getText())