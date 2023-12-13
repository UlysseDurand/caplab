.section .text
.globl main
main:
    addi t0, zero, 1
    addi t1, zero, 8
loop:
    beq t0, t1, end
    addi t0, t0, 1
    j loop
end:
    ret
