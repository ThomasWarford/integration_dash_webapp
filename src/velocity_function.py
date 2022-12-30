#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 29 2022

@author: thomas

Numerical integrators

"""

import numpy as np


def get_velocity_function(maths_strings: list):
	num_dimensions = len(maths_strings)

	if not (1 <= num_dimensions <= 3):
		raise ValueError('Number of dimensions must be between 1 and 3.')

	if num_dimensions == 1:


		def update_function_1D(x):
			return eval(maths_strings[0])

		return num_dimensions, update_function_1D

	if num_dimensions == 2:


		def update_function_2D(x, y):
			return [eval(maths_strings[0]), eval(maths_strings[1])]

		return num_dimensions, update_function_2D

	if num_dimensions == 3:


		def update_function_3D(x, y, z):
			return [eval(maths_strings[0]), eval(maths_strings[1]), eval(maths_strings[2])]

	return num_dimensions, update_function_3D



