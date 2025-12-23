from leap_year_kata.leap_year import is_leap_year


def test_4_is_leap_year():
    assert is_leap_year(4) == True


def test_5_is_leap_year():
    assert is_leap_year(5) == False


def test_year_is_divisible_by_4_is_leap_year():
    assert is_leap_year(2008) == True
    assert is_leap_year(2012) == True


def test_year_is_divisible_by_400_is_leap_year():
    assert is_leap_year(400) == True


def test_year_is_not_divisible_by_100_but_divisible_by_400_is_leap_year():
    assert is_leap_year(100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2400) == True
