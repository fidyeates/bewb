#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..op_codes import OPCodes
from .module_base import RegisterModuleFunction
from ..parser import base3_to_int, base3_to_string, string_to_base3
from ..memory import create_namespace_key


@RegisterModuleFunction(OPCodes.store_int)
def store_integer(program, ref: str, value: str):
    """
    Stores an integer {value} at reference {ref} on the heap.

    :param BewbProgram program: The program executing this function
    :param ref:
    :param value:
    :return:
    """
    heap_key = create_namespace_key(program, ref)
    program.heap.set(*heap_key, base3_to_int(value))


@RegisterModuleFunction(OPCodes.store_string)
def store_string(program, ref: str, value: str):
    """
    Stores an integer {value} at reference {ref} on the heap.

    :param BewbProgram program: The program executing this function
    :param ref:
    :param value:
    :return:
    """
    heap_key = create_namespace_key(program, ref)
    program.heap.set(*heap_key, base3_to_string(value))


CASTING_CODES = {
    0: str,
    1: int,
    2: float,
    9: string_to_base3
}


@RegisterModuleFunction(OPCodes.cast_to)
def cast_reference(program, ref: str, to_type: str, dst: str = None):
    if dst is None:
        dst = ref
    # TODO: Exception Handling
    casting_function = CASTING_CODES[base3_to_int(to_type)]

    # Get value from heap
    value = program.heap.get(*create_namespace_key(program, ref))

    heap_key = create_namespace_key(program, dst)
    program.heap.set(*heap_key, casting_function(value))
