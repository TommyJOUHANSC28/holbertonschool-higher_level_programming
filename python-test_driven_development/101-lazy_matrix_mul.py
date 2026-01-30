#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): first matrix
        m_b (list of lists of int/float): second matrix

    Returns:
        np.ndarray: result of multiplication

    Raises:
        TypeError: if input is scalar or contains non-numeric elements
        ValueError: if multiplication is impossible (handled by NumPy)
    """

    # Check if inputs are lists (scalar check)
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Check that each element of m_a and m_b is a list
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check that all elements are int or float
    for row in m_a:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")

    # Multiply using NumPy; let it handle empty matrices or incompatible shapes
    return np.matmul(m_a, m_b)
