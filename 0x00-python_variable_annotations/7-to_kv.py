#!/usr/bin/env python3
"""a type-annotated function named to_kv
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple of the string & square of v as float"""
    return (k, float(v * v))
