import pytest
from project import check_code, set_code, valid

def test_check_code():
    assert check_code('RRRR', 'RRRY') == 'You have 3 colors that are in the code and are in the right position.\nYou have 0 colors that are in the code but are in the wrong position.'

def test_set_code():
    ...

def test_valid():
    ...