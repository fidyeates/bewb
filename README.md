# Bewb

Bewb is an esoteric language (or esolang) which is aimed at immature
developers.

In principle each operation takes the form b([oO0]+)*([oO0]+)b, spelling
out 'Boob' in various lengths.



## Operation Format

An operation takes the format:

    b [op_code:16] * [variable:] ( * [variable:] )? b

All variables are unlimited length, but some op_codes
will only consider some of the length.


## Operation Codes

| Name | Code | Variables | Description |
|------|------|-----------|-------------|
| Store Char| o | char:8 ref:42 | Not Implemented |
| Store Short| O | char:16 ref:42 | Not Implemented |
| Store Int| 0 | int:32 ref:42 | Stores int at ref |
| Store Float| Oo | float:64 ref:42 | Not Implemented |
| Store Str| OO | str: ref:42 | Stores string at ref |
| Write Alpha| O0 | alpha:4N | Print alpha to screen |
| Write Whitespace| 0o | code:4 | Print whitepace to screen |
| Write Reference| 0O | ref:42 | Print reference to screen |
| Integer Addition | OoO | ref:42 ref:42 ref:42 | Adds two integers and stores result at ref |
| Define Label | 0o0 | ref:42 | Defines a label with ref |
| Go To Label | 0Oo | ref:42 | Move to execution after label at ref |
| Logical If | OoOo | left:42 right:42 operator:3 success:42 fail:42 | |
| Stdin Read | OOOO | ref:42 | Reads from stdin to ref |
| User Input | OOO0 | ref:42 ?prompt:42 | Prompts for user input into ref |
| Cast To | 000o | ref:42 type:3 | Casts value at ref to type |
| Function Define | 0o0o | ref:42 [args:42]? | Defines a function with arguments |
| Function Return | 0o00 | ref:42 | Returns the value at ref to the caller |
| Function Call | 00oo | ref:42 return:42 [args:42]? | Calls the function at ref with return value and arguments |


## Examples

A program which takes two numbers from the command line and adds them together:

    booOO*ooOoo00ooOOoOoooOOOooooOOo0o
          oooOoO0ooOOo0oooOo0o0ooOOo0O
          ooOOOooooOOoooooOOo00oooOoO0
          ooOo00oooOOo0Oooo0oOOoooOoO0
          *0b
    bOOO0*Oo*ooo0O0oooOOoo0ooOOo00ooOo0o
             0ooOOo0ooooOoO0ooOoO0OoooOo
             O0ooOOoo0ooOOOooooOOooOooOo
             O00ooOo0o0ooOOo0oooo0oOOooo
             OoO0b
    bOOO0*OO*ooo0O0oooOOoo0ooOOo00ooOo0o
             0ooOOo0ooooOoO0ooOoO0OoooOo
             O0ooOOoo0ooOOOooooOOooOooOo
             O00ooOo0o0ooOOo0oooo0oOOooo
             OoO0b
    bO00o*Oo*Ob
    bO00o*OO*Ob
    bOoO*Oo*OO*O0b
    boo0O*0b
    boo0O*O0b
    b0o*Ob

 A function based example of the above code:

    b0o0o*Oooo*OooO*OoOob
        bOoO*OoOo*OooO*Ooo0b
        b0o00*Ooo0b

    b0o0o*OOOOb
        bOOO0*OOO0*ooo0o00oooOoO0b
        bO00o*OOO0*Ob
        b0o00*OOO0b

    b0Ooo*OOOO*Oo*b
    b0Ooo*OOOO*OO*b
    b0Ooo*Oooo*O0*OO*Oob

    boo0O*O0b
    b0o*Ob