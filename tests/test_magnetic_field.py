import math 

from src.magnetic_field import helmholtz_field_at_center
def test_helmholtz_field_at_center() -> None:
    result = helmholtz_field_at_center(current=1.0, radius=0.10, turns=100)
    expected = 8.99176285573213e-4
    assert math.isclose(result, expected, rel_tol=1e-12)