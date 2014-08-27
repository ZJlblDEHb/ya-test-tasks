# -*- coding: utf-8 -*-


__author__ = 'asergeev'


from operator import itemgetter
from nose.tools import assert_equals
from task_1 import lists_to_dict


def test_task_1_list_to_dict_equal_length():
    """
    task_1.lists_to_dict should return dict with keys from first list and values from second list.
    """
    input_data = ([1, 2, 3], [1, 2, 3])
    expected_data = {1: 1, 2: 2, 3: 3}
    result = lists_to_dict(*input_data)

    assert_equals(sorted(expected_data.items(), key=itemgetter(0)), sorted(result.items(), key=itemgetter(0)))


def test_task_1_list_to_dict_values():
    """
    task_1.lists_to_dict should return dict with keys from first list and values from second list and length equal to
    list with keys.
    """
    input_data = ([1, 2], [1, 2, 3])
    expected_data = {1: 1, 2: 2}
    result = lists_to_dict(*input_data)

    assert_equals(sorted(expected_data.items(), key=itemgetter(0)), sorted(result.items(), key=itemgetter(0)))


def test_task_1_list_to_dict_keys():
    """
    task_1.lists_to_dict should return dict with keys from first list and values from second list and contains empty
    values with None.
    """
    input_data = ([1, 2, 3], [1, 2])
    expected_data = {1: 1, 2: 2, 3: None}
    result = lists_to_dict(*input_data)

    assert_equals(sorted(expected_data.items(), key=itemgetter(0)), sorted(result.items(), key=itemgetter(0)))
