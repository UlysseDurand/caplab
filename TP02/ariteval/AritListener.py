# Generated from Arit.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AritParser import AritParser
else:
    from AritParser import AritParser

# header - mettre les d??clarations globales
import sys
idTab = {};

def testID(idtext):
    if idtext not in idTab: # Always true, for now
       raise UnknownIdentifier(idtext)

class UnknownIdentifier(Exception):
    pass

class DivByZero(Exception):
    pass



# This class defines a complete listener for a parse tree produced by AritParser.
class AritListener(ParseTreeListener):

    # Enter a parse tree produced by AritParser#prog.
    def enterProg(self, ctx:AritParser.ProgContext):
        pass

    # Exit a parse tree produced by AritParser#prog.
    def exitProg(self, ctx:AritParser.ProgContext):
        pass


    # Enter a parse tree produced by AritParser#expr.
    def enterExpr(self, ctx:AritParser.ExprContext):
        pass

    # Exit a parse tree produced by AritParser#expr.
    def exitExpr(self, ctx:AritParser.ExprContext):
        pass


    # Enter a parse tree produced by AritParser#term.
    def enterTerm(self, ctx:AritParser.TermContext):
        pass

    # Exit a parse tree produced by AritParser#term.
    def exitTerm(self, ctx:AritParser.TermContext):
        pass


    # Enter a parse tree produced by AritParser#form.
    def enterForm(self, ctx:AritParser.FormContext):
        pass

    # Exit a parse tree produced by AritParser#form.
    def exitForm(self, ctx:AritParser.FormContext):
        pass



del AritParser