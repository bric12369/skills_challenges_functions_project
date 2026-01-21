from lib.estimate_reading_time import *

# Assumption: reading speed is 200wpm

def test_returns_0_when_num_of_words_is_0():
    assert estimate_reading_time(0) == '0 minutes'

def test_returns_1_when_num_of_words_is_200():
    assert estimate_reading_time(200) == '1 minute'

def test_returns_minutes_when_num_of_words_is_multiple_of_200():
    assert estimate_reading_time(1000) == '5 minutes'

def test_rounds_up_to_the_next_minute_when_words_not_multiple_of_200():
    assert estimate_reading_time(1) == '1 minute'