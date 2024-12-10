// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

// x = r1
// y = r2
// sum = 0
// while y > 0
    // sum = sum + y
    // y--
// z = sum

@0  
D=M         // D = RAM[0]
@x
M=D         // x = RAM[0]

@1
D=M         // D = RAM[1]
@y
M=D         // y = RAM[1]

@0
D=A         // D = 0
@sum
M=D         // sum = 0

(LOOP)      // while y > 0
    @y
    D=M
    @END
    D;JEQ   // y == 0 ?

    @x      
    D=M     // D = RAM[0]
    
    @sum
    M=D+M   // sum = sum + x

    @y
    D=M     // D = RAM[1]
    M=M-1   // y = y - 1

    @LOOP
    0;JMP

(END)
    @sum
    D=M
    @2
    M=D     // RAM[2] = sum

    @END
    0;JMP   // end