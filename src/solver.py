#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 29 2022

@author: thomas

Solve dynamical system with scipy.integrate.solve_ivp.

"""

import numpy as np
from scipy.integrate import solve_ivp


class Solver:
    def __init__(self, maths_strings: list):
        """
        Parameters:
            maths_strings: Strings corresponding with update rules (velocity/map functions)
        """
        self.num_dimensions = len(maths_strings)
        self.maths_strings = maths_strings

        if not (1 <= self.num_dimensions <= 3):
            raise ValueError("Number of dimensions must be between 1 and 3.")

        if self.num_dimensions == 1:

            def update_function_1D(x):
                return eval(maths_strings[0])

            self.update_rule = update_function_1D

        if self.num_dimensions == 2:

            def update_function_2D(x, y):
                return [eval(maths_strings[0]), eval(maths_strings[1])]

            self.update_rule = update_function_2D

        if self.num_dimensions == 3:

            def update_function_3D(x, y, z):
                return [
                    eval(maths_strings[0]),
                    eval(maths_strings[1]),
                    eval(maths_strings[2]),
                ]

            self.update_rule = update_function_3D

    def update_func(self, t, x):
        """
        Parameters:
                t: Needed to work with solve_ivp
                x (array-like): Position
        """

        return self.update_rule(*x)

    def integrate(self, initial_conditions, step_size, total_time):
        """
        Parameters;
                initial_conditions (array-like)
                step-size (float)
                total_time (float)
        """

        assert len(initial_conditions) == self.num_dimensions

        times = np.arange(0, total_time, step_size)

        output = solve_ivp(
            fun=self.update_func,
            t_span=(0, total_time),
            y0=initial_conditions,
            t_eval=times,
            dense_output=True,
        )

        return output["t"], output["y"], output["sol"]
