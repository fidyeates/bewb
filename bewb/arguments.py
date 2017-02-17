#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("file", nargs="?", help="The bewb file to run")
    parser.add_argument("--debug", "-d", action="store_const", const=True, help="If bewb should run in debug mode")
    parser.add_argument("--command", "-c", help="Provide commands as a string")
    parser.add_argument("--convert", "-C", help="Converts the provided string to bewb")
    return parser.parse_args()
