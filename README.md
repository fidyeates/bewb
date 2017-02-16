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
| Store Char| oooo | char:8 ref:42 | Stores char at ref |
| Store Short| oooO | char:16 ref:42 | Stores short at ref |
| Store Int| ooo0 | int:32 ref:42 | Stores int at ref |
| Store Float| ooOo | float:64 ref:42 | Stores float at ref |
| Store Str| ooOO | str: ref:42 | Stores string at ref |
| Write Alpha| ooO0 | alpha:4N | Print alpha to screen |
| Write Whitespace| oo0o | code:4 | Print whitepace to screen |
| Write Reference| oo0O | ref:42 | Print reference to screen |
| Integer Addition | oOoO | ref:42 ref:42 ref:42 | Adds two integers and stores result at ref |