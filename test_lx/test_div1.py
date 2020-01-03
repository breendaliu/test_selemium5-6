import pytest

from test_lx.div import div

@pytest.mark.yes
# @pytest.mark.parametrize 装饰器
@pytest.mark.parametrize("number1, number2, exception", {
    (10, 5, 2),
    (10, 2, 5),
    (1000000, 1, 1000000),
    (9, -1, -9),
    (-9, -1, 9),
})
def test_001(number1, number2, exception):
    assert div(number1, number2) == exception

@pytest.mark.yes
@pytest.mark.parametrize("t1, t2, r3", {
    ("a", 5, TypeError),
    (5, "a", TypeError)
})
def test_002(t1, t2, r3):
    assert div(t1, t2) == r3

@pytest.mark.parametrize("e1, e2, s", {
    (5, 0, None),
    (0, 5, None)
})
def test_003(e1, e2, s):
    assert div(e1, e2) == s


@pytest.mark.parametrize("f1, f2, x", {
    (0.55, 5, 0.11),
    (10, 3, 0.33333),
})
def test_004(f1, f2, x):
    assert div(f1, f2) == x

@pytest.mark.parametrize("g1, g2, y", {
    (' ', 5, TypeError),
    (10, ' ', TypeError),
})
def test_005(g1, g2, y):
    assert div(g1, g2) == y


if __name__ == "__main__":
   pytest.main(["-s", "test_div1.py"])
