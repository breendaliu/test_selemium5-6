import pytest



def div(a, b):
    return a / b
@pytest.mark.ha
def test_div_int():
    assert div(10, 2) == 5

@pytest.mark.ha
def test_div_folat():
    assert div(10, 3) == 0.33

def test_div_fu():
    assert div(10, 'a')


