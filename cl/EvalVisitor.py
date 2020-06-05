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
        ch = next(ctx.getChildren())
        return self.visit(ch) if ch == ctx.assig() else (None, self.visit(ch))

    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx: SkylineParser.AssigContext):
        ident = ctx.VAR().getText()
        valor = self.visit(ctx.expr())
        return (ident, valor)

    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx: SkylineParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(next(ctx.getChildren()))

        elif ctx.getChildCount() == 2:  # Negació
            g = ctx.getChildren()
            l = [next(g) for i in range(2)]
            return - self.visit(l[1])

        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]

            # Parèntesi
            if isinstance(l[0], tree.Tree.TerminalNode):
                return self.visit(l[1])

            # Intersecció / Replicació
            elif l[1].getSymbol().type == SkylineParser.PER:
                return self.visit(l[0]) * self.visit(l[2])

            # Unió / Desplaçament dreta
            elif l[1].getSymbol().type == SkylineParser.MES:
                return self.visit(l[0]) + self.visit(l[2])

            # Desplaçament esquerra
            elif l[1].getSymbol().type == SkylineParser.MENYS:
                return self.visit(l[0]) - self.visit(l[2])

    # Visit a parse tree produced by SkylineParser#simbol.
    def visitSimbol(self, ctx: SkylineParser.SimbolContext):
        if ctx.VAR() is not None:                       # Variable
            return self.taula_simbols[ctx.getText()]
        else:                                           # Número
            return int(ctx.getText())

    # Visit a parse tree produced by SkylineParser#skyline.
    def visitSkyline(self, ctx: SkylineParser.SkylineContext):
        ch = next(ctx.getChildren())
        if ch == ctx.edifici():                  # Edifici
            edifici = self.visit(ctx.edifici())
            return Skyline(edifici[0], edifici[1], edifici[2])
        else:
            return self.visit(ch)                # Creació composta o aleatòria

    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx: SkylineParser.EdificiContext):
        g = ctx.getChildren()
        l = [next(g).getText() for i in range(ctx.getChildCount())]
        return (int(l[1]), int(l[3]), int(l[5]))

    # Visit a parse tree produced by SkylineParser#compost.
    def visitCompost(self, ctx: SkylineParser.CompostContext):
        g = ctx.getChildren()
        edificis = []
        # Afegir cada edifici a una llista
        for i in range(ctx.getChildCount()):
            ch = next(g)
            if not isinstance(ch, tree.Tree.TerminalNode):
                edificis += [self.visit(ch)]
        # Retornar la creació composta a partir de la llista
        return Skyline(edificis)

    # Visit a parse tree produced by SkylineParser#random.
    def visitRandom(self, ctx: SkylineParser.RandomContext):
        g = ctx.getChildren()
        l = [next(g).getText() for i in range(ctx.getChildCount())]
        return Skyline(int(l[1]), int(l[3]), int(l[5]), int(l[7]), int(l[9]))
