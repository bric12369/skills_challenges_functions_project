from lib.check_correct_grammar import *

def test_returns_positive_message_when_given_sentence_with_capital_first_letter_and_ending_in_full_stop():
    assert check_correct_grammar('This is my sentence.') == 'Looks good!'

def test_accepts_full_stop_alternatives():
    assert check_correct_grammar('This is my sentence!') == 'Looks good!'

def test_informs_user_of_missing_capital():
    assert check_correct_grammar('this is my sentence.') == 'You\'re missing a capital letter.'

def test_accepts_numbers_as_suitable_sentence_starter():
    assert check_correct_grammar('2 words.') == 'Looks good!'

def test_informs_user_of_missing_terminal_punctuation():
    assert check_correct_grammar('This is my sentence') == 'You\'re missing your terminal punctuation.'

def test_informs_user_of_both_missing_capital_and_terminal_punctuation():
    assert check_correct_grammar('this is my sentence') == 'You\'re missing a capital letter and terminal punctuation.'