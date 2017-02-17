#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module handles the parsing of a bewb file into a BewbProgram object
"""
import re


def strip_whitespace(s: str) -> str:
    return "".join(s.split())


def strip_comments(s: str) -> str:
    return re.sub(r"\(.\)[\w\W]+\(.\)", "", s)


def split_commands(s: str) -> list:
    commands = []
    for raw_command in s.strip("b").split("bb"):
        op_code, *arguments = raw_command.split("*")
        commands.append((base3_to_int(op_code), arguments))
    return commands


def parse_raw(raw: str) -> list:
    return split_commands(strip_whitespace(strip_comments(raw)))


BEWB_BYTE_OFFSETS = {
    "o": 0,
    "O": 1,
    "0": 2
}
BEWB_BYTE_MAPPING = dict(zip(BEWB_BYTE_OFFSETS.values(), BEWB_BYTE_OFFSETS.keys()))


def base3_to_int(raw: str) -> int:
    value = 0
    for offset, ch in enumerate(raw[::-1]):
        value += ((3 ** offset) * BEWB_BYTE_OFFSETS[str(ch)])
    return value


def base3_to_string(raw: str) -> str:
    word_count = int(len(raw) / 7)
    buffer = []
    for i in range(word_count):
        word = raw[(i*7):((i+1)*7)]
        buffer.append(chr(base3_to_int(word) % 256))
    return "".join(buffer)


def int_to_base3(value: int) -> str:
    raise NotImplementedError


def string_to_base3(value: str) -> str:
    buffer = []
    for index, ch in enumerate(value):
        v = ord(ch)
        word = []
        while v > 0:
            word.append(BEWB_BYTE_MAPPING[v % 3])
            v = int(v // 3)
        buffer.append("".join(word)[::-1].rjust(7, "o"))
    return "".join(buffer)
