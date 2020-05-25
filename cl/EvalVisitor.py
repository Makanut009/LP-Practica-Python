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
        r = self.visit(next(ctx.getChildren()))
        return r


    # Visit a parse tree produced by SkylineParser#instruccio.
    def visitInstruccio(self, ctx:SkylineParser.InstruccioContext):
        if next(ctx.getChildren()) == ctx.assig():
            return self.visit(next(ctx.getChildren()))
        else:
            return (None, self.visit(next(ctx.getChildren())))


    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        res = self.visit(ctx.expr())
        self.taula_simbols[ctx.VAR().getText()] = res
        return (ctx.VAR().getText(), res)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        if ctx.getChildCount() == 1:
            print("un")
            return self.visit(ctx.simbol())

            # if next(ctx.getChildren()) == ctx.edifici():
            #     return self.visit(ctx.edifici())
            # else:
            #     return self.visit(ctx.simbol())

        elif ctx.getChildCount() == 2:
            print("dos")
            return - self.visit(ctx.simbol())

        elif ctx.getChildCount() == 3:
            print("tres")
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]

            if isinstance(l[0], tree.Tree.TerminalNode):
                print("Parèntesis")
                return self.visit(l[1])
                
            elif l[1].getSymbol().type == SkylineParser.PER:
                sk = self.visit(l[0]) * self.visit(l[2])
                return sk

            elif l[1].getSymbol().type == SkylineParser.MES:
                sk = self.visit(l[0]) + self.visit(l[2])
                return sk

            elif l[1].getSymbol().type == SkylineParser.MENYS:
                sk = self.visit(l[0]) - self.visit(l[2])
                return skç


    # Visit a parse tree produced by SkylineParser#simbol.
    def visitSimbol(self, ctx:SkylineParser.SimbolContext):
        if ctx.VAR() is not None:
            return self.taula_simbols[ctx.getText()]
        elif ctx.NUM() is not None:
            return int(ctx.getText())
        else:
            return self.visit(ctx.edifici())


    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        g = ctx.getChildren()
        l = [next(g).getText() for i in range(ctx.getChildCount())]
        return Skyline(int(l[1]), int(l[3]), int(l[5]))