import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from SkylineVisitor import SkylineVisitor

input_stream = InputStream(input('? '))

lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()

visitor = SkylineVisitor()
# evaluator = SkylineEvaluator()
print('Arbre:')
visitor.visit(tree)
print(tree.toStringTree(recog=parser))
# print('Resultat:')
# evaluator.visit(tree)