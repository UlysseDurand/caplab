# Generated from Arit.g4 by ANTLR 4.11.1
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
        4,1,14,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,36,8,2,10,2,12,2,39,9,2,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,3,0,1,4,4,0,2,4,6,0,2,1,0,8,9,1,
        0,6,7,50,0,9,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,46,1,0,0,0,8,10,
        3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,
        13,1,0,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,3,4,2,0,16,17,5,5,0,
        0,17,25,1,0,0,0,18,19,5,1,0,0,19,20,5,10,0,0,20,21,5,2,0,0,21,22,
        3,4,2,0,22,23,5,5,0,0,23,25,1,0,0,0,24,15,1,0,0,0,24,18,1,0,0,0,
        25,3,1,0,0,0,26,27,6,2,-1,0,27,28,3,6,3,0,28,37,1,0,0,0,29,30,10,
        3,0,0,30,31,7,0,0,0,31,36,3,4,2,4,32,33,10,2,0,0,33,34,7,1,0,0,34,
        36,3,4,2,3,35,29,1,0,0,0,35,32,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,
        0,37,38,1,0,0,0,38,5,1,0,0,0,39,37,1,0,0,0,40,47,5,11,0,0,41,47,
        5,10,0,0,42,43,5,3,0,0,43,44,3,4,2,0,44,45,5,4,0,0,45,47,1,0,0,0,
        46,40,1,0,0,0,46,41,1,0,0,0,46,42,1,0,0,0,47,7,1,0,0,0,5,11,24,35,
        37,46
    ]

class AritParser ( Parser ):

    grammarFileName = "Arit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'set'", "'='", "'('", "')'", "';'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SCOL", "PLUS", "MINUS", "MULT", "DIV", 
                      "ID", "INT", "COMMENT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_atom = 3

    ruleNames =  [ "prog", "statement", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SCOL=5
    PLUS=6
    MINUS=7
    MULT=8
    DIV=9
    ID=10
    INT=11
    COMMENT=12
    NEWLINE=13
    WS=14

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


        def getRuleIndex(self):
            return AritParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StatementListContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(AritParser.EOF, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.StatementContext)
            else:
                return self.getTypedRuleContext(AritParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = AritParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            localctx = AritParser.StatementListContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 3082) != 0):
                    break

            self.state = 13
            self.match(AritParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprInstrContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def SCOL(self):
            return self.getToken(AritParser.SCOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprInstr" ):
                listener.enterExprInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprInstr" ):
                listener.exitExprInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprInstr" ):
                return visitor.visitExprInstr(self)
            else:
                return visitor.visitChildren(self)


    class AssignInstrContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AritParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def SCOL(self):
            return self.getToken(AritParser.SCOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignInstr" ):
                listener.enterAssignInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignInstr" ):
                listener.exitAssignInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignInstr" ):
                return visitor.visitAssignInstr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = AritParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 10, 11]:
                localctx = AritParser.ExprInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(AritParser.SCOL)
                pass
            elif token in [1]:
                localctx = AritParser.AssignInstrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(AritParser.T__0)
                self.state = 19
                self.match(AritParser.ID)
                self.state = 20
                self.match(AritParser.T__1)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(AritParser.SCOL)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.multop = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.ExprContext)
            else:
                return self.getTypedRuleContext(AritParser.ExprContext,i)

        def MULT(self):
            return self.getToken(AritParser.MULT, 0)
        def DIV(self):
            return self.getToken(AritParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpr" ):
                return visitor.visitMultiplicationExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(AritParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.addop = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.ExprContext)
            else:
                return self.getTypedRuleContext(AritParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(AritParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(AritParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AritParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AritParser.AtomExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 27
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = AritParser.MultiplicationExprContext(self, AritParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 30
                        localctx.multop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.multop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = AritParser.AdditiveExprContext(self, AritParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 33
                        localctx.addop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.addop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expr(3)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AritParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdAtom" ):
                listener.enterIdAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdAtom" ):
                listener.exitIdAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdAtom" ):
                return visitor.visitIdAtom(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AritParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = AritParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = AritParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(AritParser.INT)
                pass
            elif token in [10]:
                localctx = AritParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(AritParser.ID)
                pass
            elif token in [3]:
                localctx = AritParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(AritParser.T__2)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(AritParser.T__3)
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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




