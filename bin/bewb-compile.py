#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import string
import operator

from bewb.op_codes import OPCodes

BYTE_OFFSETS = {
    'o': 0,
    'O': 1,
    '0': 2
}

BYTE_MAPPING = {
    0: 'o',
    1: 'O',
    2: '0'
}

GLOBAL_HEAP = {}

GLOBAL_INTERPRETER_FRAME_INDEX = None
FRAMES = []
LABEL_REFERENCE = {}

DEBUG_FLAG = False

# Functions
FUNCTION_REF = {}
TEMPORARY_STACK = []
SCOPES = {}

THIS_SCOPE = None
FUNCTION_END_FRAME = None
FUNCTION_RETURN_REF = None


def get_next_scope():
    return max(SCOPES.keys() or [0]) + 1


def write_alpha(encoded_words):
    letter_map = string.ascii_letters + string.digits
    word_count = int(len(encoded_words) / 4)
    buffer = []
    for i in range(word_count):
        buffer.append(letter_map[base3_to_int(encoded_words[(i*4):((i+1)*4)])])
    sys.stdout.write("".join(buffer))


def write_whitespace(word):
    whitespace_map = {
        0: " ",
        1: "\n",
    }
    sys.stdout.write(whitespace_map[base3_to_int(word)])


def store_string(encoded_word, reference):
    GLOBAL_HEAP[base3_to_int(reference)] = base3_to_ascii(encoded_word)


def store_int(encoded, reference):
    GLOBAL_HEAP[base3_to_int(reference)] = base3_to_int(encoded)


def int_add(left, right, reference):
    GLOBAL_HEAP[base3_to_int(reference)] = GLOBAL_HEAP[base3_to_int(left)] + GLOBAL_HEAP[base3_to_int(right)]


def write_reference(reference):
    sys.stdout.write(str(GLOBAL_HEAP[base3_to_int(reference)]))


def stdin_read(reference):
    GLOBAL_HEAP[base3_to_int(reference)] = sys.stdin.read()


def raw_input(reference, prompt=None):
    if prompt is not None:
        prompt = base3_to_ascii(prompt)
    GLOBAL_HEAP[base3_to_int(reference)] = input(prompt)


def cast_to(reference, target_type, dst=None):
    target_types = {
        0: str,
        1: int,
        2: float,
        9: NotImplemented
    }
    if dst is None:
        dst = reference
    target_type = target_types[base3_to_int(target_type)]
    if target_type is NotImplemented:
        target_type = ascii_to_base3
    GLOBAL_HEAP[base3_to_int(dst)] = target_type(GLOBAL_HEAP[base3_to_int(reference)])


def logical_if(left, right, op, success=None, fail=None):
    operator_map = {
        0: operator.eq,
        1: operator.ne,
        2: operator.lt,
        3: operator.le,
        4: operator.gt,
        5: operator.ge,
    }
    op = operator_map[base3_to_int(op)]
    result = op(GLOBAL_HEAP[base3_to_int(left)], GLOBAL_HEAP[base3_to_int(right)])
    if result and success:
        return LABEL_REFERENCE[base3_to_int(success)]
    elif not result and fail:
        return LABEL_REFERENCE[base3_to_int(fail)]
    # else carry on flow of program


def label(reference):
    # Stores label at reference
    LABEL_REFERENCE[base3_to_int(reference)] = GLOBAL_INTERPRETER_FRAME_INDEX
label.early_execute = True


def go_to_label(reference):
    return LABEL_REFERENCE[base3_to_int(reference)]


def f_define(reference, *args):
    FUNCTION_REF[base3_to_int(reference)] = GLOBAL_INTERPRETER_FRAME_INDEX
    if THIS_SCOPE:
        for i, arg in enumerate(args):
            GLOBAL_HEAP[base3_to_int(arg)] = GLOBAL_HEAP[base3_to_int(SCOPES[THIS_SCOPE][i])]

f_define.early_execute = True


def reset_scope():
    global THIS_SCOPE, GLOBAL_INTERPRETER_FRAME_INDEX, FUNCTION_RETURN_REF, FUNCTION_END_FRAME
    THIS_SCOPE = None
    FUNCTION_END_FRAME = None
    FUNCTION_RETURN_REF = None


def f_return(reference):
    global THIS_SCOPE
    if THIS_SCOPE:
        GLOBAL_HEAP[FUNCTION_RETURN_REF] = GLOBAL_HEAP[base3_to_int(reference)]
        target_frame = FUNCTION_END_FRAME
        reset_scope()
        return target_frame


def f_call(reference, f_ret, *args):
    global THIS_SCOPE, GLOBAL_INTERPRETER_FRAME_INDEX, FUNCTION_RETURN_REF, FUNCTION_END_FRAME
    THIS_SCOPE = get_next_scope()
    this_scope = args
    SCOPES[THIS_SCOPE] = this_scope
    FUNCTION_END_FRAME = GLOBAL_INTERPRETER_FRAME_INDEX + 1
    FUNCTION_RETURN_REF = base3_to_int(f_ret)
    return FUNCTION_REF[base3_to_int(reference)]


OPCODE_FUNCTION_MAP = {
    OPCodes.store_string: store_string,
    OPCodes.store_int: store_int,

    OPCodes.write_whitespace: write_whitespace,
    OPCodes.write_alpha: write_alpha,
    OPCodes.write_reference: write_reference,

    OPCodes.int_add: int_add,

    OPCodes.stdin_read: stdin_read,
    OPCodes.raw_input: raw_input,

    OPCodes.cast_to: cast_to,

    OPCodes.label: label,
    OPCodes.go_to_label: go_to_label,
    OPCodes.logical_if: logical_if,

    OPCodes.f_define: f_define,
    OPCodes.f_return: f_return,
    OPCodes.f_call: f_call,
}


def base3_to_int(b):
    value = 0
    for offset, ch in enumerate(b[::-1]):
        value += ((3 ** offset) * BYTE_OFFSETS[str(ch)])
    return value


def base3_to_ascii(b):
    word_count = int(len(b) / 7)
    buffer = []
    for i in range(word_count):
        word = b[(i*7):((i+1)*7)]
        buffer.append(chr(base3_to_int(word) % 256))
    return "".join(buffer)


def ascii_to_base3(c):
    buffer = []
    for index, ch in enumerate(c):
        v = ord(ch)
        word = []
        while v > 0:
            word.append(BYTE_MAPPING[v % 3])
            v = int(v // 3)
        buffer.append("".join(word)[::-1].rjust(7, "o"))
    return "".join(buffer)


def read_opcode(opcode):
    return base3_to_int(opcode)


def strip_word(word):
    """
    :param str word:
    :return:
    """
    return str(word.strip("b"))


def compile_file(filename):
    global GLOBAL_INTERPRETER_FRAME_INDEX
    with open(filename, 'r') as f:
        raw = f.read()
    words = "".join(raw.split()).lstrip('b').rstrip('b').split('bb')
    for i, word in enumerate(words):
        GLOBAL_INTERPRETER_FRAME_INDEX = i
        word = strip_word(word)
        opcode, arguments = word.split('*', 1)
        opcode = read_opcode(opcode)
        arguments = arguments.split("*")
        FRAMES.append((opcode, arguments))
        if hasattr(OPCODE_FUNCTION_MAP[opcode], "early_execute"):
            OPCODE_FUNCTION_MAP[opcode](*arguments)

    GLOBAL_INTERPRETER_FRAME_INDEX = 0
    run_program()


def run_program():
    if DEBUG_FLAG:
        print(FRAMES, LABEL_REFERENCE)
    global GLOBAL_INTERPRETER_FRAME_INDEX
    next_frame = 0
    skip_function = False

    while True:
        GLOBAL_INTERPRETER_FRAME_INDEX = next_frame
        opcode, arguments = FRAMES[next_frame]

        # Control flow for functions
        if opcode == OPCodes.f_define and not THIS_SCOPE:
            skip_function = True
        elif opcode == OPCodes.f_return:
            skip_function = False

        if DEBUG_FLAG:
            print(f"FRAME: {GLOBAL_INTERPRETER_FRAME_INDEX} {opcode} {arguments} {skip_function} {GLOBAL_HEAP}")

        if skip_function:
            next_frame += 1
            continue

        result = OPCODE_FUNCTION_MAP[opcode](*arguments)
        next_frame = result if result is not None else (next_frame + 1)
        if next_frame >= len(FRAMES):
            break
    # Program terminated


def main():
    global DEBUG_FLAG
    if "--debug" in sys.argv[1:]:
        DEBUG_FLAG = True
        sys.argv.remove("--debug")
    target = sys.argv[1]
    print("Compiling target: {}".format(target))
    compile_file(target)

if __name__ == '__main__':
    main()
