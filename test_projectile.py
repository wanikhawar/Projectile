import pytest

from projectile import Projectile  # Assume the class is in projectile.py


@pytest.fixture
def projectile():
    """Fixture to initialize a Projectile instance with sample values."""
    return Projectile(v0=50, theta=45)  # Launch at 45 degrees, v0 = 50 m/s


def test_position(projectile):
    # Check position at t = 0
    assert projectile.position(0) == (0, 0)

    # Check position at midpoint (approx)
    x, y = projectile.position(2)
    assert pytest.approx(x, 0.1) == 70.71
    assert pytest.approx(y, 0.1) == 51.11


def test_velocity(projectile):
    # Check velocity at t = 0
    vx, vy = projectile.velocity(0)
    assert pytest.approx(vx, 0.1) == 35.36
    assert pytest.approx(vy, 0.1) == 35.36

    # Check velocity at later time
    vx, vy = projectile.velocity(2)
    assert pytest.approx(vx, 0.1) == 35.36
    assert pytest.approx(vy, 0.1) == 15.36  # Reduced due to gravity


def test_horizontal_range(projectile):
    # Check calculated horizontal range
    horizontal_range = projectile.horizontal_range()
    assert pytest.approx(horizontal_range, 0.1) == 255.1


def test_time_of_flight(projectile):
    # Check calculated time of flight
    time_of_flight = projectile.time_of_flight()
    assert pytest.approx(time_of_flight, 0.1) == 7.21


def test_maximum_height(projectile):
    # Check calculated maximum height
    max_height = projectile.maximum_height()
    assert pytest.approx(max_height, 0.1) == 63.77


def test_check_valid_time_instant(projectile):
    # Test valid time
    try:
        projectile.check_valid_time_instant(3)
    except ValueError:
        pytest.fail("check_valid_time_instant raised ValueError unexpectedly")

    # Test invalid time (negative)
    with pytest.raises(ValueError):
        projectile.check_valid_time_instant(-1)

    # Test invalid time (greater than time of flight)
    with pytest.raises(ValueError):
        projectile.check_valid_time_instant(8)
    with pytest.raises(ValueError):
        projectile.check_valid_time_instant(8)
