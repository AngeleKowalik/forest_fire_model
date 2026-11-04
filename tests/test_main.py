# import pytest
import main as mn
import numpy as np
import logging as lg

lg.basicConfig(level="DEBUG")

def test_matrix_init():
    """Test if matrix initialize properly. It should create a 3*3 np array filled with 0s."""
    test = mn.Matrix(3, 3)
    oracle = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])
    assert np.all(oracle == test.matrix), f"Matrix did not initialize properly\n{test.matrix}\nIt should look like this\n{oracle}"

def test_prob_insert_1():
    """Test if probalistic_insert replace all occurence of 0 in matrix with 1s"""
    test = mn.Matrix(3, 3)
    test.probabilistic_insert(1, 0, 1)
    oracle = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]])
    assert np.all(oracle == test.matrix), f'Test matrix:\n{test.matrix}\nOracle:\n{oracle}'

def test_prob_insert_0():
    """Test if probalistic_insert does something when probability is null, it should do nothing"""
    test = mn.Matrix(3, 3)
    test.probabilistic_insert(0, 0, 1)
    oracle = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])
    assert np.all(oracle == test.matrix), f'Test matrix:\n{test.matrix}\nOracle:\n{oracle}'


def test_prob_insert():
    """Test if probabilistit_insert insert value with the provided frequency p"""
    test = mn.Matrix(3, 3)
    oracle_p = 0.3
    test_list = np.array([])
    for n in range(10000):
        test.probabilistic_insert(oracle_p, 0, 1)
        test_list = np.append(test_list, np.sum(test.matrix == 1) / 9)
        test.probabilistic_insert(1, 1, 0)
        test_mean = test_list.mean()

    assert oracle_p - 0.01 <= test_mean <= oracle_p + 0.01, f'test_list:\n{test_list}\nOracle p = {oracle_p}\nTest_p = {test_mean}'








