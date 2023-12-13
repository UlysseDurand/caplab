# Generated from Arit.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# header - mettre les d??clarations globales
import sys
idTab = {};

def valeur(idtext):
    if idtext not in idTab: # Always true, for now
        raise UnknownIdentifier(idtext)
    else:
        return idTab[idtext]

class UnknownIdentifier(Exception):
    pass

class DivByZero(Exception):
    pass



def serializedATN():
    return [
        4,0,8,53,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,4,1,30,8,1,11,1,12,1,31,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,
        6,4,6,43,8,6,11,6,12,6,44,1,7,4,7,48,8,7,11,7,12,7,49,1,7,1,7,0,
        0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,3,2,0,10,10,13,13,2,0,
        65,90,97,122,3,0,9,10,13,13,32,32,56,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,1,17,1,0,0,0,3,29,1,0,0,0,5,33,1,0,0,0,7,35,1,0,0,0,9,37,1,
        0,0,0,11,39,1,0,0,0,13,42,1,0,0,0,15,47,1,0,0,0,17,18,5,47,0,0,18,
        19,5,47,0,0,19,23,1,0,0,0,20,22,8,0,0,0,21,20,1,0,0,0,22,25,1,0,
        0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,
        6,0,0,0,27,2,1,0,0,0,28,30,7,1,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,4,1,0,0,0,33,34,5,43,0,0,34,6,1,0,0,
        0,35,36,5,42,0,0,36,8,1,0,0,0,37,38,5,40,0,0,38,10,1,0,0,0,39,40,
        5,41,0,0,40,12,1,0,0,0,41,43,2,48,57,0,42,41,1,0,0,0,43,44,1,0,0,
        0,44,42,1,0,0,0,44,45,1,0,0,0,45,14,1,0,0,0,46,48,7,2,0,0,47,46,
        1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,
        51,52,6,7,0,0,52,16,1,0,0,0,5,0,23,31,44,49,1,6,0,0
    ]

class AritLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    ID = 2
    PLUS = 3
    TIMES = 4
    LPAR = 5
    RPAR = 6
    INT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "ID", "PLUS", "TIMES", "LPAR", "RPAR", "INT", "WS" ]

    ruleNames = [ "COMMENT", "ID", "PLUS", "TIMES", "LPAR", "RPAR", "INT", 
                  "WS" ]

    grammarFileName = "Arit.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


