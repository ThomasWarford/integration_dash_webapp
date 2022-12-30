#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 29 2022

@author: thomas

Test numerical integrator.

"""

from velocity_function import get_velocity_function
from solver import Solver
import matplotlib.pyplot as plt
import numpy as np


def test_circle():
    # should produce clockwise circlular orbit
    epsilon = 0.1  # for testing purposes

    circle_strings = [
        "y",
        "-x",
    ]

    initial_conditions = [3.0, 4.0]  # circle should have radius 5
    step_size = 0.1
    final_time = 50

    num_dimensions, v_func = get_velocity_function(circle_strings)

    solver = Solver(num_dimensions, v_func)
    t, x, sol = solver.integrate(initial_conditions, step_size, final_time)

    assert (np.abs(sol.__call__(2 * np.pi) - initial_conditions) <= epsilon).all()
    assert (abs(x[0] ** 2 + x[1] ** 2 - 25.0) < epsilon).all(), abs(
        x[0] ** 2 + x[1] ** 2 - 25.0
    )
    print(t)
    print(x)

    fig, ax = plt.subplots()
    ax.plot(x[0], x[1])

    ax.set_xlim([-6, 6])
    ax.set_ylim([-6, 6])
    ax.grid()
    plt.show()


def test_lorenz_attractor():
    # purely visual test
    epsilon = 0.001  # small change in initial conditions, examining chaos

    lorenz_strings = ["10 * (y - x)", "28*x - y - x*z", "x* y - 8/3 * z"]

    initial_conditions_1 = np.array([1.0, 1.0, 1.0])  # circle should have radius 5
    initial_conditions_2 = initial_conditions_1 + epsilon
    step_size = 0.01
    final_time = 50

    num_dimensions, v_func = get_velocity_function(lorenz_strings)

    solver = Solver(num_dimensions, v_func)
    t1, x1, sol1 = solver.integrate(initial_conditions_1, step_size, final_time)
    t2, x2, sol2 = solver.integrate(initial_conditions_2, step_size, final_time)

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot(x1[0], x1[1], x1[2])
    ax.plot(x2[0], x2[1], x2[2])

    plt.show()


def main():
    # test_circle()
    test_lorenz_attractor()  # looks good !


if __name__ == "__main__":
    main()
