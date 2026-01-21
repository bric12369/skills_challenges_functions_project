def count_words(string):
    if len(string) == 0:
        return 0
    else:
        words = string.split(' ')
        return len(words)