# -*- coding: utf-8 -*-


__author__ = 'asergeev'


from itertools import izip_longest


def lists_to_dict(keys_list, values_list):
    """
    Produces dict from given lists with keys and values.
    :param keys_list: list with keys
    :param values_list: list with values
    :return: dict like {keys_list[0]: values_list[0], ... }
    """
    return {key: value for key, value in izip_longest(keys_list, values_list) if key is not None}