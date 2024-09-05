# DAY OF THE WEEK TEST

# START

def test_day_sunday():
    assert day_of_week(1) == "Sunday"

def test_day_monday():
    assert day_of_week(2) == "Monday"

def test_day_tuesday():
    assert day_of_week(3) == "Tuesday"

def test_day_wednesday():
    assert day_of_week(4) == "Wednesday"

def test_day_thursday():
    assert day_of_week(5) == "Thursday"

def test_day_friday():
    assert day_of_week(6) == "Friday"

def test_day_saturday():
    assert day_of_week(7) == "Saturday"

# Test for out-of-range day
def test_invalid_day():
    try:
        day_of_week(0)
    except ValueError as e:
        assert str(e) == "Invalid day number"
    else:
        assert False

# END