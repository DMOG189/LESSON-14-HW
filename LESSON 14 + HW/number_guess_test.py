# NUMBER GUESS TEST

# START

# Test when the guess is correct
def test_guess_correct():
    assert check_guess(50, '50') == "BINGO"

# Test when the guess is lower than the lucky number
def test_guess_lower():
    assert check_guess(50, '40') == "higher guess"

# Test when the guess is higher than the lucky number
def test_guess_higher():
    assert check_guess(50, '60') == "lower guess"

# Test invalid input (non-numeric string)
def test_invalid_input():
    try:
        check_guess(50, 'forty-two')
    except ValueError:
        assert True
    else:
        assert False

# Test out-of-range input (above 100)
def test_out_of_range():
    try:
        check_guess(50, '144')
    except ValueError as e:
        assert str(e) == "number out of range"
    else:
        assert False

# Test out-of-range input (negative number)
def test_negative_number():
    try:
        check_guess(50, '-5')
    except ValueError as e:
        assert str(e) == "number out of range"
    else:
        assert False

# END