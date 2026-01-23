#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices using numpy
    """

    # Vérifier que m_a et m_b sont des listes
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Vérifier qu’ils ne sont pas vides
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Vérifier que chaque élément est une liste
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Vérifier que les éléments sont int ou float
    for row in m_a:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")

    # Vérifier que la multiplication est possible
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiplier
    try:
        return np.matmul(m_a, m_b)
    except Exception:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
