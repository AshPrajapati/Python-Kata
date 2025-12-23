from leap_year_kata.leap_year import is_leap_year


def test_4_is_leap_year():
    assert is_leap_year(4) == True


def test_5_is_leap_year():
    assert is_leap_year(5) == False


def test_year_is_divisible_by_4_is_leap_year():
    assert is_leap_year(2008) == True
    assert is_leap_year(2012) == True
