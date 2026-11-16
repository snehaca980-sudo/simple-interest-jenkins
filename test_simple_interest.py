
from simple_interest import simInt

def test_simInt():
    assert simInt(1000, 5, 2) == 100
    assert simInt(2000, 10, 3) == 600
