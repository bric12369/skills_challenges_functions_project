from lib.make_snippet import *

def test_returns_whole_string_when_given_string_of_5_words():
    assert make_snippet('These are my five words.') == 'These are my five words.'

def test_returns_first_5_words_of_string_with_ellipses_for_strings_longer_than_5():
    assert make_snippet('There are more than five words in this string') == 'There are more than five...'

def test_returns_string_if_empty_or_less_than_5_words():
    assert make_snippet('') == ''
    assert make_snippet('Two words') == 'Two words'

def test_returns_full_string_if_given_string_without_spaces():
    assert make_snippet('This_string_has_more_than_5_words_but_no_spaces') == 'This_string_has_more_than_5_words_but_no_spaces'