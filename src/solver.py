#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 29 2022

@author: thomas

Solve dynamical system with scipy.integrate.solve_ivp.

"""

from typing import Callable
import numpy as np
from scipy.integrate import solve_ivp


class Solver:
    def __init__(self, num_dimensions: int, velocity_function: Callable):
        """
        Parameters:
                num_dimensions: Number of dimensions of numerical system.
                functions (list): Strings containing x, y, z which give rate of change of each variable, taking 3 variables as an input.
        """

        self.num_dimensions = num_dimensions
        self.velocity_function = velocity_function

    def v_func(self, t, x):
        """
        Parameters:
                t: Needed to work with solve_ivp
                x (array-like): Position
        """

        return self.velocity_function(*x)

    def integrate(self, initial_conditions, step_size, total_time):
        """USE ODE THING!
        Parameters;
                initial_conditions (array-like)
                step-size (float)
                total_time (float)
        """

        assert len(initial_conditions) == self.num_dimensions

        times = np.arange(0, total_time, step_size)

        output = solve_ivp(
            fun=self.v_func,
            t_span=(0, total_time),
            y0=initial_conditions,
            t_eval=times,
            dense_output=True,
        )

        return output["t"], output["y"], output["sol"]
