def check_correct_grammar(sentence):
    terminal_punctuation = ['.', '!', '?']
    capital_letter_first = sentence[0] == sentence[0].upper()
    ends_with_terminal_punctuation = sentence[-1] in terminal_punctuation
    if not capital_letter_first and not ends_with_terminal_punctuation:
        return 'You\'re missing a capital letter and terminal punctuation.'
    elif not capital_letter_first:
        return 'You\'re missing a capital letter.'
    elif not ends_with_terminal_punctuation:
        return 'You\'re missing your terminal punctuation.'
    else:
        return 'Looks good!'