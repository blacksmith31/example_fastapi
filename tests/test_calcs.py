
import pytest
from app.calcs import add

@pytest.mark.parametrize("n1, n2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(n1, n2, expected):
    print("testing add function")
    assert add(n1, n2) == expected