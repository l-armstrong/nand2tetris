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

(START)
    @8192
    D=A
    @i
    M=D

(START_LOOP)
    @i
    M=M-1
    D=M
    @START
    D;JLT               // check if i < 0
    
    @KBD                // poll current keyboard press
    D=M
    @DRAW_WHITE_SCREEN  // If key input is 0, no key is being press, draw white Screen
    D;JEQ
    @DRAW_BLACK_SCREEN
    0;JMP

(DRAW_BLACK_SCREEN)
    @SCREEN
    D=A                // load register for screen
    @i
    A=D+M               // offset from base screen address to draw current pixel
    M=-1                // set 16 pixels to black
    @START_LOOP         // go decrement the current offset
    0;JMP

(DRAW_WHITE_SCREEN)
    @SCREEN
    D=A                // load register for screen
    @i
    A=D+M               // offset from base screen address to draw current pixel
    M=0                 // set 16 pixels to white
    @START_LOOP         // go decrement the current offset
    0;JMP