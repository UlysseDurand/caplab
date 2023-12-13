# Generated from Arit.g4 by ANTLR 4.11.1
# encoding: utf-8
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

def testID(idtext):
    if idtext not in idTab: # Always true, for now
       raise UnknownIdentifier(idtext)

class UnknownIdentifier(Exception):
    pass

class DivByZero(Exception):
    pass


def serializedATN():
    return [
        4,1,8,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,41,8,
        3,1,3,0,2,2,4,4,0,2,4,6,0,0,42,0,8,1,0,0,0,2,11,1,0,0,0,4,22,1,0,
        0,0,6,40,1,0,0,0,8,9,3,2,1,0,9,10,6,0,-1,0,10,1,1,0,0,0,11,12,6,
        1,-1,0,12,13,3,4,2,0,13,19,1,0,0,0,14,15,10,2,0,0,15,16,5,3,0,0,
        16,18,3,4,2,0,17,14,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,
        0,0,0,20,3,1,0,0,0,21,19,1,0,0,0,22,23,6,2,-1,0,23,24,3,6,3,0,24,
        30,1,0,0,0,25,26,10,2,0,0,26,27,5,4,0,0,27,29,3,6,3,0,28,25,1,0,
        0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,5,1,0,0,0,32,30,
        1,0,0,0,33,34,5,2,0,0,34,41,6,3,-1,0,35,41,5,7,0,0,36,37,5,5,0,0,
        37,38,3,2,1,0,38,39,5,6,0,0,39,41,1,0,0,0,40,33,1,0,0,0,40,35,1,
        0,0,0,40,36,1,0,0,0,41,7,1,0,0,0,3,19,30,40
    ]

class AritParser ( Parser ):

    grammarFileName = "Arit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "ID", "PLUS", "TIMES", "LPAR", 
                      "RPAR", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_form = 3

    ruleNames =  [ "prog", "expr", "term", "form" ]

    EOF = Token.EOF
    COMMENT=1
    ID=2
    PLUS=3
    TIMES=4
    LPAR=5
    RPAR=6
    INT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)


        def getRuleIndex(self):
            return AritParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = AritParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            localctx._expr = self.expr(0)
            print("prog = "+str((None if localctx._expr is None else self._input.getText(localctx._expr.start,localctx._expr.stop))));
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

        def term(self):
            return self.getTypedRuleContext(AritParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)


        def PLUS(self):
            return self.getToken(AritParser.PLUS, 0)

        def getRuleIndex(self):
            return AritParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AritParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AritParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 14
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 15
                    self.match(AritParser.PLUS)
                    self.state = 16
                    self.term(0) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form(self):
            return self.getTypedRuleContext(AritParser.FormContext,0)


        def term(self):
            return self.getTypedRuleContext(AritParser.TermContext,0)


        def TIMES(self):
            return self.getToken(AritParser.TIMES, 0)

        def getRuleIndex(self):
            return AritParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AritParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.form()
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AritParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 25
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 26
                    self.match(AritParser.TIMES)
                    self.state = 27
                    self.form() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FormContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(AritParser.ID, 0)

        def INT(self):
            return self.getToken(AritParser.INT, 0)

        def LPAR(self):
            return self.getToken(AritParser.LPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(AritParser.RPAR, 0)

        def getRuleIndex(self):
            return AritParser.RULE_form

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForm" ):
                listener.enterForm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForm" ):
                listener.exitForm(self)




    def form(self):

        localctx = AritParser.FormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_form)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                localctx._ID = self.match(AritParser.ID)
                testID((None if localctx._ID is None else localctx._ID.text));
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(AritParser.INT)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(AritParser.LPAR)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(AritParser.RPAR)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




