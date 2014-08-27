# -*- coding: utf-8 -*-


__author__ = 'asergeev'


from nose.tools import assert_equals
from task_2 import validate_login, bad_validate_login


def test_task_2_validate_login_valid_input():
    """
    task_2.validate_login should return True for valid input string.
    """
    input_data = 'Julius.Caesar-2000'
    expected_data = True
    result = validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_validate_login_first_symbol_dot():
    """
    task_2.validate_login should return False if first symbol of the string is dot.
    """
    input_data = '.another.Julius'
    expected_data = False
    result = validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_validate_login_last_symbol_dash():
    """
    task_2.validate_login should return False if last symbol of the string is dash.
    """
    input_data = 'another.Julius-'
    expected_data = False
    result = validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_validate_login_one_symbol_length():
    """
    task_2.validate_login should return True if length of the string is 1.
    """
    input_data = 'J'
    expected_data = True
    result = validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_validate_login_more_then_20_length():
    """
    task_2.validate_login should return False if length of the string is more then 20.
    """
    input_data = 'The.Greatest.Julius.Caesar-3000'
    expected_data = False
    result = validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_bad_validate_login_valid_input():
    """
    task_2.bad_validate_login should return True for valid input string.
    """
    input_data = 'Julius.Caesar-2000'
    expected_data = True
    result = bad_validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_bad_validate_login_first_symbol_dot():
    """
    task_2.bad_validate_login should return False if first symbol of the string is dot.
    """
    input_data = '.another.Julius'
    expected_data = False
    result = bad_validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_bad_validate_login_last_symbol_dash():
    """
    task_2.bad_validate_login should return False if last symbol of the string is dash.
    """
    input_data = 'another.Julius-'
    expected_data = False
    result = bad_validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_bad_validate_login_one_symbol_length():
    """
    task_2.bad_validate_login should return True if length of the string is 1.
    """
    input_data = 'J'
    expected_data = True
    result = bad_validate_login(input_data)

    assert_equals(result, expected_data)


def test_task_2_bad_validate_login_more_then_20_length():
    """
    task_2.bad_validate_login should return False if length of the string is more then 20.
    """
    input_data = 'The.Greatest.Julius.Caesar-3000'
    expected_data = False
    result = bad_validate_login(input_data)

    assert_equals(result, expected_data)