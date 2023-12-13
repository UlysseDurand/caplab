from typing import List, Tuple
from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser
from Lib.LinearCode import LinearCode
from Lib import RiscV
from Lib.RiscV import Condition
from Lib import Operands
from antlr4.tree.Trees import Trees
from Lib.Errors import MiniCInternalError, MiniCUnsupportedError

"""
CAP, MIF08, three-address code generation + simple alloc
This visitor constructs an object of type "LinearCode".
"""


class MiniCCodeGen3AVisitor(MiniCVisitor):

    _current_function: LinearCode

    def __init__(self, debug, parser):
        super().__init__()
        self._parser = parser
        self._debug = debug
        self._functions = []
        self._lastlabel = ""

    def get_functions(self) -> List[LinearCode]:
        return self._functions

    def printSymbolTable(self):  # pragma: no cover
        print("--variables to temporaries map--")
        for keys, values in self._symbol_table.items():
            print(keys + '-->' + str(values))

    # handle variable decl

    def visitVarDecl(self, ctx) -> None:
        type_str = ctx.typee().getText()
        vars_l = self.visit(ctx.id_l())
        for name in vars_l:
            if name in self._symbol_table:
                raise MiniCInternalError(
                    "Variable {} has already been declared".format(name))
            else:
                tmp = self._current_function.fdata.fresh_tmp()
                self._symbol_table[name] = tmp
                if type_str not in ("int", "bool"):
                    raise MiniCUnsupportedError("Unsupported type " + type_str)
                # Initialization to 0 or False, both represented with 0
                self._current_function.add_instruction(
                    RiscV.li(tmp, Operands.Immediate(0)))

    def visitIdList(self, ctx) -> List[str]:
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx) -> List[str]:
        return [ctx.ID().getText()]

    # expressions

    def visitParExpr(self, ctx) -> Operands.Temporary:
        return self.visit(ctx.expr())

    # To visit Atoms, we get its value, allocate a temp and load it in.

    def visitIntAtom(self, ctx) -> Operands.Temporary:
        val = Operands.Immediate(int(ctx.getText()))
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.li(dest_temp, val))
        return dest_temp

    def visitFloatAtom(self, ctx) -> Operands.Temporary:
        raise MiniCUnsupportedError("float literal")

    def visitBooleanAtom(self, ctx) -> Operands.Temporary:
        # true is 1 false is 0
        match ctx.getText():
            case "true":
                val = Operands.Immediate(1)
            case "false":
                val = Operands.Immediate(0)
            case other:
                # Should be syntactically unreachable
                raise MiniCInternalError("Bool value should be either true of false")
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.li(dest_temp, val))
        return dest_temp

    def visitIdAtom(self, ctx) -> Operands.Temporary:
        try:
            # get the temporary associated to id
            return self._symbol_table[ctx.getText()]
        except KeyError:  # pragma: no cover
            raise MiniCInternalError(
                "Undefined variable {}, this should have failed to typecheck."
                .format(ctx.getText())
            )

    def visitStringAtom(self, ctx) -> Operands.Temporary:
        raise MiniCUnsupportedError("string atom")

    # now visit expressions

    def visitAtomExpr(self, ctx) -> Operands.Temporary:
        return self.visit(ctx.atom())

    def visitAdditiveExpr(self, ctx) -> Operands.Temporary:
        assert ctx.myop is not None
        tmpl: Operands.Temporary = self.visit(ctx.expr(0))
        tmpr: Operands.Temporary = self.visit(ctx.expr(1))
        dest_temp = self._current_function.fdata.fresh_tmp()
        match ctx.myop.type:
            case MiniCParser.PLUS:
                self._current_function.add_instruction(RiscV.add(dest_temp,tmpl,tmpr))
            case MiniCParser.MINUS:
                self._current_function.add_instruction(RiscV.sub(dest_temp,tmpl,tmpr))
        return dest_temp

    def visitOrExpr(self, ctx) -> Operands.Temporary:
        tmpl: Operands.Temporary = self.visit(ctx.expr(0))
        tmpr: Operands.Temporary = self.visit(ctx.expr(1))
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.lor(dest_temp,tmpl,tmpr))
        return dest_temp


    def visitAndExpr(self, ctx) -> Operands.Temporary:
        tmpl: Operands.Temporary = self.visit(ctx.expr(0))
        tmpr: Operands.Temporary = self.visit(ctx.expr(1))
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.land(dest_temp,tmpl,tmpr))
        return dest_temp

    def visitEqualityExpr(self, ctx) -> Operands.Temporary:
        return self.visitRelationalExpr(ctx)

    def visitRelationalExpr(self, ctx) -> Operands.Temporary:
        assert ctx.myop is not None
        c = Condition(ctx.myop.type)
        if self._debug:
            print("relational expression:")
            print(Trees.toStringTree(ctx, [], self._parser))
            print("Condition:", c)
        # Initialise as usual
        dest_temp = self._current_function.fdata.fresh_tmp()
        tmpl: Operands.Temporary = self.visit(ctx.expr(0))
        tmpr: Operands.Temporary = self.visit(ctx.expr(1))
        # Create a label that returns 1
        endrel_lbl = self._current_function.fdata.fresh_label("end_relational")
        self._current_function.add_instruction(RiscV.li(dest_temp,Operands.Immediate(1)))
        # If the relation is verified, jump to label
        self._current_function.add_instruction(RiscV.conditional_jump(endrel_lbl, tmpl, c, tmpr))
        # else return 0
        self._current_function.add_instruction(RiscV.li(dest_temp,Operands.Immediate(0)))
        self._current_function.add_label(endrel_lbl)
        return dest_temp

    def visitMultiplicativeExpr(self, ctx) -> Operands.Temporary:
        assert ctx.myop is not None
        div_by_zero_lbl = self._current_function.fdata.get_label_div_by_zero()
        tmpl: Operands.Temporary = self.visit(ctx.expr(0))
        tmpr: Operands.Temporary = self.visit(ctx.expr(1))
        dest_temp = self._current_function.fdata.fresh_tmp()
        match ctx.myop.type:
            case MiniCParser.MULT:
                self._current_function.add_instruction(RiscV.mul(dest_temp,tmpl,tmpr))
            case MiniCParser.DIV:
                # If the right operad is zero we jump to the label
                self._current_function.add_instruction(RiscV.conditional_jump(div_by_zero_lbl,Operands.ZERO, Condition("beq"),tmpr))
                # Else we divide
                self._current_function.add_instruction(RiscV.div(dest_temp,tmpl,tmpr))
            case MiniCParser.MOD:
                self._current_function.add_instruction(RiscV.conditional_jump(div_by_zero_lbl,Operands.ZERO, Condition("beq"),tmpr))
                self._current_function.add_instruction(RiscV.rem(dest_temp,tmpl,tmpr))
        return dest_temp

    def visitNotExpr(self, ctx) -> Operands.Temporary:
        # Since bools are 0 or 1, (1 - b) = not b
        tmpr: Operands.Temporary = self.visit(ctx.expr())
        tmpl = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.li(tmpl,Operands.Immediate(1)))
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.sub(dest_temp,tmpl,tmpr))
        return dest_temp

    def visitUnaryMinusExpr(self, ctx) -> Operands.Temporary:
        # Taking the unary Minus is equivalent to subtracting from 0
        tmpl = Operands.ZERO
        tmpr: Operands.Temporary = self.visit(ctx.expr())
        dest_temp = self._current_function.fdata.fresh_tmp()
        self._current_function.add_instruction(RiscV.sub(dest_temp,tmpl,tmpr))
        return dest_temp

    def visitProgRule(self, ctx) -> None:
        self.visitChildren(ctx)

    def visitFuncDef(self, ctx) -> None:
        funcname = ctx.ID().getText()
        self._current_function = LinearCode(funcname)
        self._symbol_table = dict()

        self.visit(ctx.vardecl_l())
        self.visit(ctx.block())
        self._current_function.add_comment("Return at end of function:")
        # This skeleton doesn't deal properly with functions, and
        # hardcodes a "return 0;" at the end of function. Generate
        # code for this "return 0;".
        self._current_function.add_instruction(
        	RiscV.li(Operands.A0, Operands.Immediate(0)))
        self._functions.append(self._current_function)
        del self._current_function

    def visitAssignStat(self, ctx) -> None:
        if self._debug:
            print("assign statement, rightexpression is:")
            print(Trees.toStringTree(ctx.expr(), [], self._parser))
        expr_temp = self.visit(ctx.expr())
        name = ctx.ID().getText()
        self._current_function.add_instruction(RiscV.mv(self._symbol_table[name], expr_temp))

    def visitIfStat(self, ctx) -> None:
        if self._debug:
            print("if statement")
        end_if_label = self._current_function.fdata.fresh_label("end_if")
        else_label = self._current_function.fdata.fresh_label("else")
        tmp = self.visit(ctx.expr())
        # If the condition is false, jump to Else
        self._current_function.add_instruction(RiscV.conditional_jump(else_label, tmp, Condition("beq"), Operands.ZERO))
        self.visit(ctx.stat_block(0)) # Then code
        self._current_function.add_instruction(RiscV.jump(end_if_label)) # After running jump to end
        self._current_function.add_label(else_label)
        if ctx.else_block :
            self.visit(ctx.stat_block(1)) # Else code
        self._current_function.add_label(end_if_label)

    def visitWhileStat(self, ctx) -> None:
        if self._debug:
            print("while statement, condition is:")
            print(Trees.toStringTree(ctx.expr(), [], self._parser))
            print("and block is:")
            print(Trees.toStringTree(ctx.stat_block(), None, self._parser))
        test_while_label = self._current_function.fdata.fresh_label("begin_while")
        end_while_label = self._current_function.fdata.fresh_label("end_while")
        self._current_function.add_label(test_while_label)
        tmp: Operands.Temporary = self.visit(ctx.expr())
        #if the condition is false jump to end
        self._current_function.add_instruction(RiscV.conditional_jump(end_while_label, tmp, Condition("beq"), Operands.ZERO))
        self.visit(ctx.stat_block()) # Else run body code
        self._current_function.add_instruction(RiscV.jump(test_while_label)) # And jump back to condition
        self._current_function.add_label(end_while_label)

    # visit statements

    def visitPrintlnintStat(self, ctx) -> None:
        expr_loc = self.visit(ctx.expr())
        if self._debug:
            print("print_int statement, expression is:")
            print(Trees.toStringTree(ctx.expr(), [], self._parser))
        self._current_function.add_instruction_PRINTLN_INT(expr_loc)

    def visitPrintlnboolStat(self, ctx) -> None:
        expr_loc = self.visit(ctx.expr())
        self._current_function.add_instruction_PRINTLN_INT(expr_loc)

    def visitPrintlnfloatStat(self, ctx) -> None:
        raise MiniCUnsupportedError("Unsupported type float")

    def visitPrintlnstringStat(self, ctx) -> None:
        raise MiniCUnsupportedError("Unsupported type string")

    def visitStatList(self, ctx) -> None:
        for stat in ctx.stat():
            self._current_function.add_comment(Trees.toStringTree(stat, [], self._parser))
            self.visit(stat)
