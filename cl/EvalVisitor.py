from antlr4 import *
from Skyline import Skyline

if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser


class EvalVisitor(ParseTreeVisitor):

    def __init__(self, ts):
        self.taula_simbols = ts

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx: SkylineParser.RootContext):
        r = self.visit(next(ctx.getChildren()))
        return r

    # Visit a parse tree produced by SkylineParser#instruccio.
    def visitInstruccio(self, ctx: SkylineParser.InstruccioContext):
        if next(ctx.getChildren()) == ctx.assig():
            return self.visit(next(ctx.getChildren()))
        else:
            return (None, self.visit(next(ctx.getChildren())))

    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx: SkylineParser.AssigContext):
        res = self.visit(ctx.expr())
        self.taula_simbols[ctx.VAR().getText()] = res
        return (ctx.VAR().getText(), res)

    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx: SkylineParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(next(ctx.getChildren()))
            # ch = next(ctx.getChildren())
            # if ch == ctx.simbol():
            #     return self.visit(ctx.simbol())
            # elif ch == ctx.simbol():

        elif ctx.getChildCount() == 2:
            return - self.visit(ctx.simbol())

        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]

            if isinstance(l[0], tree.Tree.TerminalNode):
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
    def visitSimbol(self, ctx: SkylineParser.SimbolContext):
        if ctx.VAR() is not None:
            return self.taula_simbols[ctx.getText()]
        elif ctx.NUM() is not None:
            return int(ctx.getText())
        else:
            edifici = self.visit(ctx.edifici())
            return Skyline(edifici[0], edifici[1], edifici[2])

    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx: SkylineParser.EdificiContext):
        g = ctx.getChildren()
        l = [next(g).getText() for i in range(ctx.getChildCount())]
        return (int(l[1]), int(l[3]), int(l[5]))

    # Visit a parse tree produced by SkylineParser#compost.
    def visitCompost(self, ctx: SkylineParser.CompostContext):
        g = ctx.getChildren()
        edificis = []
        for i in range(ctx.getChildCount()):
            ch = next(g)
            if not isinstance(ch, tree.Tree.TerminalNode):
                edificis += [self.visit(ch)]
        return Skyline(edificis)

    # Visit a parse tree produced by SkylineParser#random.
    def visitRandom(self, ctx: SkylineParser.RandomContext):
        g = ctx.getChildren()
        l = [next(g).getText() for i in range(ctx.getChildCount())]
        return Skyline(int(l[1]), int(l[3]), int(l[5]), int(l[7]), int(l[9]))
