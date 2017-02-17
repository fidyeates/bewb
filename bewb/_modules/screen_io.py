#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from ..op_codes import OPCodes
from .module_base import RegisterModuleFunction
from ..memory import create_namespace_key
from ..parser import base3_to_string


@RegisterModuleFunction(OPCodes.write_reference)
def print_reference(program, ref: str):
    heap_key = create_namespace_key(program, ref)
    sys.stdout.write(str(program.heap.get(*heap_key)))


@RegisterModuleFunction(OPCodes.write_ln)
def print_ln(_):
    sys.stdout.write("\n")


@RegisterModuleFunction(OPCodes.raw_input)
def b_raw_input(program, ref: str, prompt: str =None):
    if prompt:
        prompt = base3_to_string(prompt)
    user_input = input(prompt)
    heap_key = create_namespace_key(program, ref)
    program.heap.set(*heap_key, user_input)
