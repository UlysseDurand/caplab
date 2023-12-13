# Generated from Example4.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,22,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,0,0,2,0,2,0,0,22,0,4,1,0,0,0,
        2,19,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,5,1,0,0,8,9,
        3,2,1,0,9,10,5,2,0,0,10,11,3,2,1,0,11,20,1,0,0,0,12,13,5,3,0,0,13,
        14,3,2,1,0,14,15,5,4,0,0,15,16,3,2,1,0,16,20,1,0,0,0,17,20,5,5,0,
        0,18,20,1,0,0,0,19,7,1,0,0,0,19,12,1,0,0,0,19,17,1,0,0,0,19,18,1,
        0,0,0,20,3,1,0,0,0,1,19
    ]

class Example4Parser ( Parser ):

    grammarFileName = "Example4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "OPAR", "CPAR", "OBRA", "CBRA", "ID", 
                      "WS" ]

    RULE_full_expr = 0
    RULE_expr = 1

    ruleNames =  [ "full_expr", "expr" ]

    EOF = Token.EOF
    OPAR=1
    CPAR=2
    OBRA=3
    CBRA=4
    ID=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Full_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Example4Parser.ExprContext,0)


        def EOF(self):
            return self.getToken(Example4Parser.EOF, 0)

        def getRuleIndex(self):
            return Example4Parser.RULE_full_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_expr" ):
                listener.enterFull_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_expr" ):
                listener.exitFull_expr(self)




    def full_expr(self):

        localctx = Example4Parser.Full_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_full_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(Example4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPAR(self):
            return self.getToken(Example4Parser.OPAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Example4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Example4Parser.ExprContext,i)


        def CPAR(self):
            return self.getToken(Example4Parser.CPAR, 0)

        def OBRA(self):
            return self.getToken(Example4Parser.OBRA, 0)

        def CBRA(self):
            return self.getToken(Example4Parser.CBRA, 0)

        def ID(self):
            return self.getToken(Example4Parser.ID, 0)

        def getRuleIndex(self):
            return Example4Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = Example4Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(Example4Parser.OPAR)
                self.state = 8
                self.expr()
                self.state = 9
                self.match(Example4Parser.CPAR)
                self.state = 10
                self.expr()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(Example4Parser.OBRA)
                self.state = 13
                self.expr()
                self.state = 14
                self.match(Example4Parser.CBRA)
                self.state = 15
                self.expr()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.match(Example4Parser.ID)
                pass
            elif token in [-1, 2, 4]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





