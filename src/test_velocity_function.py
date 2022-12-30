#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 29 2022

@author: thomas

Tests for velocity_function.py
"""


from velocity_function import get_velocity_function
import numpy as np


def test_velocity_function_1D():
	strings = [
	'x**3 - 3*x**2 * 4',
	]

	num_dimensions, v_func = get_velocity_function(strings)


	assert num_dimensions == 1
	assert v_func(2.) == -40.

def test_velocity_function_2D():
	strings = [
	'-y',
	'-x',
	]

	num_dimensions, v_func = get_velocity_function(strings)


	assert num_dimensions == 2
	assert v_func(1., 1.) == [-1., -1.]

def test_velocity_function_3D():
	strings = [
	'np.cos(np.pi * (x + y)) + z',
	'- y * np.cos(np.pi * x) - z',
	'-z'
	]

	num_dimensions, v_func = get_velocity_function(strings)


	assert num_dimensions == 3
	assert v_func(.25, .25, 1) == [1., -np.sqrt(2.)/8. - 1, -1.]


def main():
	test_velocity_function_1D()
	test_velocity_function_2D()
	test_velocity_function_3D()


if __name__ == '__main__':
	main()