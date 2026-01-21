from lib.count_words import *

def test_count_words_returns_0_when_passed_empty_string():
    assert count_words('') == 0

def test_count_words_returns_1_when_passed_one_word():
    assert count_words('One') == 1

def test_counts_words_in_string_and_returns():
    assert count_words('One, two, three, four, five.') == 5

def test_only_counts_words_as_those_separated_by_spaces():
    assert count_words('No_spaces_here') == 1