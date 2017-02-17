#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Routines to handle the heap
"""
from .parser import base3_to_int

NAMESPACES = set()


def get_next_namespace() -> int:
    if NAMESPACES:
        next_namespace = max(NAMESPACES) + 1
    else:
        next_namespace = 0
    NAMESPACES.add(next_namespace)
    return next_namespace


class Heap(object):

    def __init__(self):
        self._heap = {}

    def set(self, namespace: int, ref: int, value):
        self._heap[(namespace, ref)] = value

    def get(self, namespace: int, ref: int, default=None):
        if default:
            return self._heap.get((namespace, ref), default)
        else:
            return self._heap[(namespace, ref)]

    def __repr__(self):
        return repr(self._heap)


def create_namespace_key(program, reference) -> tuple:
    if isinstance(reference, str):
        reference = base3_to_int(reference)
    return program.current_namespace, reference
