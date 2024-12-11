// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// while True
//  check if key register == 0
//      if so make screen white
//      else make screen black

(MAIN_LOOP) 
    @KBD    // RAM[24576]
    D=M     // D=RAM[24576] // read contents of key
    @WHITE_SCREEN
    D;JEQ   // if key == 0; make screen white

    @SCREEN
    D=A
    @addr
    M=D     // addr = 16384

    // i = 0 
        // while i < 256
        // j = 0
        // while j < 32
        //  set RAM[addr] = -1
        // j + 1
        // addr = addr + 1
    // i = i + 1
    @0
    D=A
    @i
    M=D     // i = 0

    (OUTER_LOOP)    // while i < 256
        @256
        D=A
        @i
        D=D-M       // 256 - i
        @MAIN_LOOP
        D;JEQ  // i == 256 jump to MainLOOP 

        @0       
        D=A     // put 0 in D for j  
        @j
        M=D     // set j = 0

        (INNER_LOOP) // while j < 32
            @32
            D=A
            @j
            D=D-M
            @OUTER_LOOP
            D;JEQ   // j == 32

            @addr
            A=M
            M=-1        // RAM[addr]=111111111....

            @j
            M=M+1       // j = j + 1
            @addr
            M=M+1       // addr = addr + 1
            
            @INNER_LOOP
            0;JMP

   // @MAIN_LOOP
    //0;JMP
(WHITE_SCREEN)

    @SCREEN
    D=A
    @addr
    M=D     // addr = 16384

    // i = 0 
        // while i < 256
        // j = 0
        // while j < 32
        //  set RAM[addr] = -1
        // j + 1
        // addr = addr + 1
    // i = i + 1
    @0
    D=A
    @i
    M=D     // i = 0

    (WHITE_OUTER_LOOP)    // while i < 256
        @256
        D=A
        @i
        D=D-M       // 256 - i
        @MAIN_LOOP
        D;JEQ  // i == 256 jump to MainLOOP 

        @0       
        D=A     // put 0 in D for j  
        @j
        M=D     // set j = 0

        (WHITE_INNER_LOOP) // while j < 32
            @32
            D=A
            @j
            D=D-M
            @WHITE_OUTER_LOOP
            D;JEQ   // j == 32

            @addr
            A=M
            M=0        // RAM[addr]=000000000000....

            @j
            M=M+1       // j = j + 1
            @addr
            M=M+1       // addr = addr + 1
            
            @WHITE_INNER_LOOP
            0;JMP
    //@MAIN_LOOP
    // 0;JMP