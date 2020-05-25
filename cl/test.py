import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from EvalVisitor import EvalVisitor

from skyline import Skyline

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))

print(type(input_stream))

lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()
#print(tree.toStringTree(recog=parser))

visitor = EvalVisitor()
visitor.visit(tree)

# visitor = SkylineVisitor()
# # evaluator = SkylineEvaluator()
# print('Arbre:')
# visitor.visit(tree)
# print(tree.toStringTree(recog=parser))
# print(visitor.taula_simbols)
# # print('Resultat:')
# # evaluator.visit(tree)