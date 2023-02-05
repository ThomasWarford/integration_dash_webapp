#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 29 2022

@author: thomas

Tests for velocity_function.py
"""


from solver import Solver
import numpy as np


def test_velocity_function_1D():
    strings = [
        "x**3 - 3*x**2 * 4",
    ]

    solver = Solver(strings)

    # num_dimensions, v_func = get_velocity_function(strings)

    assert solver.num_dimensions == 1
    assert solver.update_rule(2.0) == -40.0


def test_velocity_function_2D():
    strings = [
        "-y",
        "-x",
    ]

    solver = Solver(strings)

    assert solver.num_dimensions == 2
    assert solver.update_rule(1.0, 1.0) == [-1.0, -1.0]


def test_velocity_function_3D():
    strings = ["np.cos(np.pi * (x + y)) + z", "- y * np.cos(np.pi * x) - z", "-z"]

    solver = Solver(strings)

    assert solver.num_dimensions == 3
    assert solver.update_rule(0.25, 0.25, 1) == [1.0, -np.sqrt(2.0) / 8.0 - 1, -1.0]


def main():
    test_velocity_function_1D()
    test_velocity_function_2D()
    test_velocity_function_3D()


if __name__ == "__main__":
    main()
