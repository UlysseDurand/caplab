.section .text
.globl main
main:
    addi a0, zero, 0
    addi t0, zero, 0
    addi t1, zero, 10
loop:
    beq t0, t1, end
    addi t0, t0, 1
    add a0, a0, t0
    j loop
end:
    call print_int
    call newline
    ret
