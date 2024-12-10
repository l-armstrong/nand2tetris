// Program: rect.asm
// Draws a filled rectangle at the
// screens top left left corner, with
// width of 16 pixels and height of
// RAM[0] pixels.
// Usage: put a non-negative number
//  (rectanges height) in RAM[0].

@SCREEN
D=A
@addr
M=D     // addr = 16384
        // screens base address
@0      // rectangles height
D=M
@n
M=D     // n = RAM[0]

@i
M=0     // i = 0 

(LOOP)
    @i
    D=M
    @n
    D=D-M   // n - i
    @END
    D;JGT   // if i>n goto END

    @addr
    A=M
    M=-1    // RAM[addr]=1111111111....

    @i
    M=M+1   // i = i + 1
    @32
    D=A
    @addr
    M=D+M   // addr = addr + 32
    @LOOP
    0;JMP   // goto LOOP

(END)
    @END    // programs end
    0;JMP   // infinite loop