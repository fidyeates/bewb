#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Required imports for decorator patching
from .bewb_types import *
from .screen_io import *
from .arithmatic import *
from .control_flow import *

from .module_base import OP_CODE_FUNCTION_REGISTRY
from ..exceptions import BewbRuntimeError


def get_function_by_opcode(op_code: int) -> callable:
    if op_code not in OP_CODE_FUNCTION_REGISTRY:
        raise BewbRuntimeError(f"No such op_code: {op_code}")
    return OP_CODE_FUNCTION_REGISTRY[op_code]
