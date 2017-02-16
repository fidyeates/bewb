#!/usr/bin/env python
# -*- coding: utf-8 -*-


class OPCodes:
    store_char = NotImplemented
    store_short = NotImplemented
    store_int = 2
    store_float = NotImplemented
    store_string = 4
    store_alpha = NotImplemented

    write_alpha = 5
    write_whitespace = 6
    write_reference = 7

    int_add = 10
    int_div = NotImplemented
    int_sub = NotImplemented
    int_mul = NotImplemented
    int_pow = NotImplemented

    label = 20
    go_to_label = 21

    logical_if = 30

    # File I/O
    stdin_read = 40  # ref:
    raw_input = 41  # ref:
    file_open = NotImplemented
    file_read = NotImplemented
    file_write = NotImplemented

    cast_to = 51  # type: ref: ?dst:

    f_define = 60
    f_arg_init = 61
    f_return = 62
    f_call = 63

    str_concat = NotImplemented
    str_replace = NotImplemented
