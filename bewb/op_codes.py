#!/usr/bin/env python
# -*- coding: utf-8 -*-


class OPCodes:
    # Variable Definitions
    store_int = 2
    store_string = 4

    # Screen I/O
    write_alpha = 5
    write_whitespace = 6
    write_reference = 7
    write_ln = 8

    # Integer arithmetic
    int_add = 10
    int_div = NotImplemented
    int_sub = NotImplemented
    int_mul = NotImplemented
    int_pow = NotImplemented

    # Control Flow
    label = 20
    go_to_label = 21

    logical_if = 30

    # File I/O
    stdin_read = 40  # ref:
    raw_input = 41  # ref:
    file_open = NotImplemented
    file_read = NotImplemented
    file_write = NotImplemented

    # Type Casting
    cast_to = 51  # type: ref: ?dst:

    # Functions
    f_define = 60
    f_arg_init = 61
    f_return = 62
    f_call = 63

    # String Methods
    str_concat = NotImplemented
    str_replace = NotImplemented
