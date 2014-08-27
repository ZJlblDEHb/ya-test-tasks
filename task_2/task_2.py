# -*- coding: utf-8 -*-


__author__ = 'asergeev'


import re
import string


REGEXP = r'[a-z]{1,1}(([a-z0-9.\-]{0,18}[a-z0-9]{1,1}$)|$)'

FIRST_SYMBOL_RANGE = string.ascii_lowercase
LAST_SYMBOL_RANGE = string.ascii_lowercase + ''.join([str(number) for number in range(10)])
STANDARD_SYMBOL_RANGE = LAST_SYMBOL_RANGE + '.-'


def validate_login(login):
    """
    Validates given login string by regexp.
    :param login: string with login
    :return: True if login string is matched, else False
    """
    return True if re.match(REGEXP, login, re.IGNORECASE) is not None else False


def bad_validate_login(login):
    """
    Validates given login string by several criteria
    :param login: string with login
    :return: True if login string is matched, else False
    """
    length = len(login)
    lower = login.lower()

    if 1 > length or length > 20:
        return False

    if lower[0] not in FIRST_SYMBOL_RANGE:
        return False
    elif length == 1:
        return True

    if lower[length-1] not in LAST_SYMBOL_RANGE:
        return False

    for symbol in lower[1:-1]:
        if symbol not in STANDARD_SYMBOL_RANGE:
            return False

    return True