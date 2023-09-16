import pytest
from project import check_code, set_code, valid, CHOICES

def test_check_code():
    assert check_code('RRRR', 'RRRY') == 'You have 3 colors that are in the code and are in the right position.\nYou have 0 colors that are in the code but are in the wrong position.'

# Checks if set code makes a valid code
def test_set_code():
    code = set_code()
    for i in code:
        assert i in CHOICES


def test_valid():
    with pytest.raises(ValueError):
        valid('RRYY', 'cat')
    with pytest.raises(ValueError):
        valid('RRYY', 'RRYYY')
    with pytest.raises(ValueError):
        valid('RRYY', 'RR')
