# Generated from Skyline.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#instruccio.
    def visitInstruccio(self, ctx:SkylineParser.InstruccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#simbol.
    def visitSimbol(self, ctx:SkylineParser.SimbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#compost.
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#random.
    def visitRandom(self, ctx:SkylineParser.RandomContext):
        return self.visitChildren(ctx)



del SkylineParser