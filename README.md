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
| Store Char| oooo | char:8 ref:42 | Not Implemented |
| Store Short| oooO | char:16 ref:42 | Not Implemented |
| Store Int| ooo0 | int:32 ref:42 | Stores int at ref |
| Store Float| ooOo | float:64 ref:42 | Not Implemented |
| Store Str| ooOO | str: ref:42 | Stores string at ref |
| Write Alpha| ooO0 | alpha:4N | Print alpha to screen |
| Write Whitespace| oo0o | code:4 | Print whitepace to screen |
| Write Reference| oo0O | ref:42 | Print reference to screen |
| Integer Addition | oOoO | ref:42 ref:42 ref:42 | Adds two integers and stores result at ref |
| Define Label | 0o0 | ref:42 | Defines a label with ref |
| Go To Label | 0Oo | ref:42 | Move to execution after label at ref |
| Logical If | OoOo | left:42 right:42 operator:3 success:42 fail:42 | |
| Stdin Read | OOOO | ref:42 | Reads from stdin to ref |
| User Input | OOO0 | ref:42 ?prompt:42 | Prompts for user input into ref |
| Cast To | 000o | ref:42 type:3 | Casts value at ref to type |
| Function Define | 0o0o | ref:42 [args:42]? | Defines a function with arguments |
| Function Return | 0o00 | ref:42 | Returns the value at ref to the caller |
| Function Call | 00oo | ref:42 return:42 [args:42]? | Calls the function at ref with return value and arguments |
