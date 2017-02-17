#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..exceptions import BewbRuntimeError


OP_CODE_FUNCTION_REGISTRY = {}


class RegisterModuleFunction(object):

    def __init__(self, op_code: int, preprocess: bool = False):
        self.op_code = op_code
        self.preprocess = preprocess

    def __call__(self, fn: callable) -> callable:
        if self.op_code in OP_CODE_FUNCTION_REGISTRY:
            raise BewbRuntimeError(f"op_code: {self.op_code} already registered")
        OP_CODE_FUNCTION_REGISTRY[self.op_code] = fn
        fn.preprocess = self.preprocess
        return fn
