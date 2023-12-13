# Visitor to *typecheck* MiniC files
from typing import List, NoReturn
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Lib.Errors import MiniCInternalError, MiniCTypeError

from enum import Enum


class BaseType(Enum):
    Float, Integer, Boolean, String = range(4)


# Basic Type Checking for MiniC programs.
class MiniCTypingVisitor(MiniCVisitor):

    def __init__(self):
        self._memorytypes = dict()  # id -> types
        # For now, we don't have real functions ...
        self._current_function = "main"

    def _raise(self, ctx, for_what, *types):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: invalid type for {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, for_what,
                ' and '.join(t.name.lower() for t in types)))

    def _assertSameType(self, ctx, for_what, *types):
        if not all(types[0] == t for t in types):
            raise MiniCTypeError(
                'In function {}: Line {} col {}: type mismatch for {}: {}'.format(
                    self._current_function,
                    ctx.start.line, ctx.start.column, for_what,
                    ' and '.join(t.name.lower() for t in types)))

    def _raiseNonType(self, ctx, message) -> NoReturn:
        raise MiniCTypeError(
            'In function {}: Line {} col {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, message))

    # type declaration

    def visitVarDecl(self, ctx) -> None:
        typee = self.visit(ctx.typee())
        ids = self.visit(ctx.id_l())
        for id_str in ids:
            if id_str in self._memorytypes:
                raise MiniCTypeError(
                    'In function {}: Line {} col {}: Variable {} already declared'.format(
                        self._current_function,
                        ctx.start.line, ctx.start.column, id_str))
            self._memorytypes[id_str] = typee

    def visitBasicType(self, ctx):
        assert ctx.mytype is not None
        if ctx.mytype.type == MiniCParser.INTTYPE:
            return BaseType.Integer
        elif ctx.mytype.type == MiniCParser.FLOATTYPE:
            return BaseType.Float
        elif ctx.mytype.type == MiniCParser.STRINGTYPE:
            return BaseType.String
        elif ctx.mytype.type == MiniCParser.BOOLTYPE:
            return BaseType.Boolean
        else:
            raise MiniCInternalError(
                f"Unknown basic type '{ctx.mytype.type}'")

    def visitIdList(self, ctx) -> List[str]:
        tail = self.visit(ctx.id_l())
        head = ctx.ID().getText()
        tail.insert(0,head)
        return tail

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # typing visitors for expressions, statements !

    # visitors for atoms --> type
    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitIntAtom(self, ctx):
        return BaseType.Integer

    def visitFloatAtom(self, ctx):
        return BaseType.Float

    def visitBooleanAtom(self, ctx):
        return BaseType.Boolean

    def visitIdAtom(self, ctx):
        try:
            return self._memorytypes[ctx.getText()]
        except KeyError:
            self._raiseNonType(ctx,
                               "Undefined variable {}".format(ctx.getText()))

    def visitStringAtom(self, ctx):
        return BaseType.String

    # now visit expr

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx):
        ltype = self.visit(ctx.expr(0))
        rtype = self.visit(ctx.expr(1))
        if ltype != BaseType.Boolean:
            self._raise(ctx, 'Or operands', ltype, rtype)
        if rtype != BaseType.Boolean:
            self._raise(ctx, 'Or operands', ltype, rtype)
        return BaseType.Boolean

    def visitAndExpr(self, ctx):
        ltype = self.visit(ctx.expr(0))
        rtype = self.visit(ctx.expr(1))
        if ltype != BaseType.Boolean:
            self._raise(ctx, 'And operands', ltype, rtype)
        if rtype != BaseType.Boolean:
            self._raise(ctx, 'And operands', ltype, rtype)
        return BaseType.Boolean

    def visitEqualityExpr(self, ctx):
        ltype = self.visit(ctx.expr(0))
        rtype = self.visit(ctx.expr(1))
        self._assertSameType(ctx, 'Equality operands', ltype, rtype)
        return BaseType.Boolean

    def visitRelationalExpr(self, ctx):
        assert ctx.myop is not None
        ltype = self.visit(ctx.expr(0))
        rtype = self.visit(ctx.expr(1))
        if not (ltype in [BaseType.Integer, BaseType.Float]):
            self._raise(ctx, 'relational operands', ltype, rtype)
        if not (rtype in [BaseType.Integer, BaseType.Float]):
            self._raise(ctx, 'relational operands', ltype, rtype)
        self._assertSameType(ctx, 'relational operands', ltype, rtype)
        return BaseType.Boolean

    def visitAdditiveExpr(self, ctx):
        assert ctx.myop is not None
        ltype = self.visit(ctx.expr(0))
        rtype = self.visit(ctx.expr(1))
        if not (ltype in [BaseType.Integer, BaseType.Float, BaseType.String]):
            self._raise(ctx, 'additive operands', ltype, rtype)
        if not (rtype in [BaseType.Integer, BaseType.Float, BaseType.String]):
            self._raise(ctx, 'additive operands', ltype, rtype)
        self._assertSameType(ctx, 'additive operands', ltype, rtype)
        return ltype

    def visitMultiplicativeExpr(self, ctx):
        assert ctx.myop is not None
        ltype = self.visit(ctx.expr(0))
        rtype = self.visit(ctx.expr(1))
        if ctx.myop.type == MiniCParser.MOD:
            if not (ltype == BaseType.Integer and rtype == BaseType.Integer):
                self._raise(ctx, 'modulo operands', ltype, rtype)
            return ltype
        else:
            if not (ltype in [BaseType.Integer, BaseType.Float]):
                self._raise(ctx, 'multiplicative operands', ltype, rtype)
            if not (rtype in [BaseType.Integer, BaseType.Float]):
                self._raise(ctx, 'multiplicative operands', ltype, rtype)
            self._assertSameType(ctx, 'multiplicative operands', ltype, rtype)
            return ltype

    def visitNotExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Boolean:
            self._raise(ctx, 'Not operand', etype)
        return BaseType.Boolean

    def visitUnaryMinusExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if not (etype in [BaseType.Integer, BaseType.Float]) :
            self._raise(ctx, 'Unary Minus operand', etype)
        return etype

    # visit statements

    def visitPrintlnintStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Integer:
            self._raise(ctx, 'println_int statement', etype)

    def visitPrintlnfloatStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Float:
            self._raise(ctx, 'println_float statement', etype)

    def visitPrintlnboolStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Boolean:
            self._raise(ctx, 'println_bool statement', etype)

    def visitPrintlnstringStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.String:
            self._raise(ctx, 'println_string statement', etype)

    def visitAssignStat(self, ctx):
        id_str = ctx.ID().getText()
        try:
            id_type = self._memorytypes[id_str]
        except KeyError:
            self._raiseNonType(ctx,
                               "Undefined variable {}".format(id_str))
        etype = self.visit(ctx.expr())
        self._assertSameType(ctx, id_str, id_type, etype)

    def visitWhileStat(self, ctx):
        typecond = self.visit(ctx.expr())
        typebody = self.visit(ctx.body)
        if typecond != BaseType.Boolean:
            self._raise(ctx, "While condition", typecond)

    def visitForStat(self, ctx):
        typecond = self.visit(ctx.cond)
        typebody = self.visit(ctx.body)
        if ctx.init_a:
            self.visit(ctx.init_a)
        if ctx.incr_a:
            self.visit(ctx.incr_a)
        if typecond != BaseType.Boolean:
            self._raise(ctx, "For condition", typecond)

    def visitIfStat(self, ctx):
        typecond = self.visit(ctx.expr())
        typethen = self.visit(ctx.then_block)
        if ctx.else_block:
            typeelse = self.visit(ctx.else_block)
        if typecond != BaseType.Boolean:
            self._raise(ctx, "If condition", typecond)
        # self._assertSameType(ctx, "Then and Else blocks", typethen, typeelse)
        # return typethen
