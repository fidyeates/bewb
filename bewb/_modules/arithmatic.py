#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..op_codes import OPCodes
from .module_base import RegisterModuleFunction
from ..memory import create_namespace_key


@RegisterModuleFunction(OPCodes.int_add)
def integer_addition(program, left: str, right: str, dst: str):
    left_key = create_namespace_key(program, left)
    right_key = create_namespace_key(program, right)
    dst_key = create_namespace_key(program, dst)
    result = program.heap.get(*left_key) + program.heap.get(*right_key)
    program.heap.set(*dst_key, result)
