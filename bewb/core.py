#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bewb runtime objects and functionality
"""
from collections import deque

from .exceptions import BewbRuntimeError
from ._modules import get_function_by_opcode
from .arguments import parse_arguments
from .memory import Heap, get_next_namespace
from .parser import parse_raw, string_to_base3


class Frame(object):

    def __init__(self, op_code: int, arguments: list):
        self.op_code: int = op_code
        self.arguments: list = arguments

    def __repr__(self):
        return f"Frame(op_code={self.op_code}, arguments={self.arguments})"


class BewbProgram(object):

    def __init__(self, frames: list, start_frame: int =0, debug=False):
        self.frames: list = frames
        self._current_frame_index = start_frame
        self.heap = Heap()

        # Labels
        self.labels = {}

        # Namespaces
        self.global_namespace = get_next_namespace()
        self.current_namespace = self.global_namespace
        self.namespace_stack = deque()

        self._debug = debug
        self.debug(f"Program running frames: {frames} with start index: {start_frame}")

    def get_frame_at_index(self, index: int) -> Frame:
        """

        :param int index: The index of the frame to fetch
        :return:
        """
        if not self.frame_in_bounds(index):
            raise BewbRuntimeError(f"Can't access frame at index: {index}")
        return self.frames[index]

    def frame_in_bounds(self, index: int):
        return index < len(self.frames)

    @property
    def current_index(self) -> int:
        return self._current_frame_index

    @property
    def current_frame(self) -> Frame:
        return self.get_frame_at_index(self.current_index)

    def set_next_frame(self, value: int):
        self._current_frame_index = value

    def increment_frame_index(self):
        self._current_frame_index += 1

    def preprocess(self):
        hold_frame = self.current_index
        self._current_frame_index = 0
        for frame in self.frames:
            preprocess_frame(self, frame)
            self.increment_frame_index()
        self._current_frame_index = hold_frame

    def debug(self, message):
        if self._debug:
            print(message)

    def get_label_index(self, reference: str):
        return self.labels[reference]

    def set_label_index(self, reference: str, index: int):
        self.labels[reference] = index

    def run(self):
        self.debug(f"Program labels: {self.labels}")
        while True:
            current_index = self.current_index

            if not self.frame_in_bounds(current_index):
                break

            frame = self.current_frame

            self.debug(f"({current_index}) Executing Frame: {frame}\n\tHeap: {self.heap}")

            next_frame = execute_frame(self, frame)

            if next_frame:
                self.set_next_frame(next_frame)
            else:
                self.increment_frame_index()
        self.debug(f"Program exiting with heap: {self.heap}")

    def garbage_collect_namespace(self, namespace):
        raise NotImplementedError


def execute_frame(program: BewbProgram, frame: Frame) -> int:
    """
    Executes the frame at
    :param program:
    :param frame:
    :return:
    """
    return get_function_by_opcode(frame.op_code)(program, *frame.arguments)


def preprocess_frame(program: BewbProgram, frame: Frame):
    """

    :param program:
    :param frame:
    :return:
    """
    frame_function = get_function_by_opcode(frame.op_code)
    if frame_function.preprocess:
        program.debug(f"Pre processing frame: {frame}")
        frame_function(program, *frame.arguments)


def main():
    arguments = parse_arguments()
    raw_frames = []
    if arguments.command:
        raw_frames = parse_raw(arguments.command)
    elif arguments.convert:
        print(string_to_base3(arguments.convert))
        exit(0)
    else:
        with open(arguments.file, 'r') as f:
            raw_frames = parse_raw(f.read())
    frames = [Frame(*raw_frame) for raw_frame in raw_frames]
    program = BewbProgram(frames, debug=arguments.debug)
    program.preprocess()
    program.run()
