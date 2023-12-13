from Lib import RiscV
from Lib.Operands import Temporary, Operand, S
from Lib.Statement import Instruction
from Lib.Allocator import Allocator
from typing import List, Dict


class AllInMemAllocator(Allocator):

    def replace(self, old_instr: Instruction) -> List[Instruction]:
        """Replace Temporary operands with the corresponding allocated
        memory location."""
        # numreg is the least unused S register index
        numreg = 1
        before: List[Instruction] = []
        after: List[Instruction] = []
        subst: Dict[Operand, Operand] = {}
        # If old_instr only reads its arguments
        if old_instr.is_read_only():
            for arg in old_instr.args():
                if isinstance(arg, Temporary):
                    # We need only to load the temporaries from the stack
                    before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                    subst[arg] = S[numreg]
                    numreg +=1 # This will never go over three as there are at most 3 args
        # Else we must store the result in the stack
        else:
            for (i, arg) in enumerate(old_instr.args()):
                # The only destination is always the first argument
                if i == 0:
                    if isinstance(arg, Temporary):
                        # The destination register is S[1]
                        subst[arg] = S[1]
                        after.append(RiscV.sd(S[1], arg.get_alloced_loc()))
                        numreg +=1
                # The rest are all read only
                else:
                    if isinstance(arg, Temporary):
                        before.append(RiscV.ld(S[numreg], arg.get_alloced_loc()))
                        subst[arg] = S[numreg]
                        numreg +=1
        new_instr = old_instr.substitute(subst)
        return before + [new_instr] + after

    def prepare(self) -> None:
        """Allocate all temporaries to memory.
        Invariants:
        - Expanded instructions can use s2 and s3
          (to store the values of temporaries before the actual instruction).
        """
        self._fdata._pool.set_temp_allocation(
            {temp: self._fdata.fresh_offset()
             for temp in self._fdata._pool.get_all_temps()})
