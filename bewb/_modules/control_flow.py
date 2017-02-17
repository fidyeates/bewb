#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..op_codes import OPCodes
from .module_base import RegisterModuleFunction
from ..parser import base3_to_int


@RegisterModuleFunction(OPCodes.label, preprocess=True)
def create_label(program, ref: str):
    """
    Creates a label with reference {ref}
    :param BewbProgram program:
    :param ref:
    :return:
    """
    program.set_label_index(base3_to_int(ref), program.current_index)


@RegisterModuleFunction(OPCodes.go_to_label)
def go_to_label(program, ref: str):
    """
    Moves control flow of the program to label
    :param program:
    :param ref:
    :return:
    """
    return program.get_label_index(base3_to_int(ref))
