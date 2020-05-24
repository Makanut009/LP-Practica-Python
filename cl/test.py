import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser

input_stream = InputStream(input('? '))

lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))

# visitor = SkylineVisitor()
# # evaluator = SkylineEvaluator()
# print('Arbre:')
# visitor.visit(tree)
# print(tree.toStringTree(recog=parser))
# print(visitor.taula_simbols)
# # print('Resultat:')
# # evaluator.visit(tree)