"""
CAP, SSA Intro, Elimination and Optimisations
Functions to convert a CFG out of SSA Form.
"""

from typing import cast, List
from Lib import RiscV
from Lib.CFG import Block, BlockInstr, CFG
from Lib.Operands import Temporary, DataLocation
from Lib.Statement import AbsoluteJump
from Lib.Terminator import BranchingTerminator, Return
from Lib.PhiNode import PhiNode
from TP05.SequentializeMoves import sequentialize_moves


def generate_moves_from_phis(phis: List[PhiNode], parent: Block) -> List[BlockInstr]:
    """
    `generate_moves_from_phis(phis, parent)` builds a list of move instructions
    to be inserted in a new block between `parent` and the block with phi nodes
    `phis`.

    This is an helper function called during SSA exit.
    """
    moves: List[BlockInstr] = []

    for phi in phis:
        lessrcs = phi.get_srcs()
        labelparent = parent.get_label()
        if labelparent in lessrcs:
            lasrc = lessrcs[labelparent]
            if isinstance(lasrc,DataLocation):
                lavar = phi.defined()[0]
                moves.append(RiscV.mv(lavar,lasrc))


    # (Lab 5a, Exercise 6)
    return moves


def exit_ssa(cfg: CFG, is_smart: bool) -> None:
    """
    `exit_ssa(cfg)` replaces phi nodes with move instructions to exit SSA form.

    `is_smart` is set to true when smart register allocation is enabled (Lab 5b).
    """
    for b in cfg.get_blocks():
        phis = cast(List[PhiNode], b.get_phis())  # Use cast for Pyright
        b.remove_all_phis()  # Remove all phi nodes in the block
        parents: List[Block] = b.get_in().copy()  # Copy as we modify it by adding blocks
        for parent in parents:
            moves = generate_moves_from_phis(phis, parent)
            labelblock = cfg.fdata.fresh_label("block")
            term = AbsoluteJump(b.get_label())
            nvblock = Block(labelblock,moves,term)
            cfg.add_block(nvblock)

            parterm = parent.get_terminator()
            if isinstance(parterm, BranchingTerminator):
                if (parterm.label_then == b.get_label()):
                    thenlabel = labelblock
                    elselabel = parterm.label_else
                else:
                    thenlabel = parterm.label_then
                    elselabel = labelblock
                parent.set_terminator(BranchingTerminator(parterm.cond, parterm.op1, parterm.op2, thenlabel, elselabel))
            elif isinstance(parent.get_terminator(), Return):
                pass
            else:
                parent.set_terminator(AbsoluteJump(nvblock.get_label()))

            cfg.remove_edge(parent,b)
            cfg.add_edge(parent, nvblock)
            cfg.add_edge(nvblock, b)
