import math

def estimate_reading_time(num_of_words):
        minutes = math.ceil(num_of_words/200)
        if minutes == 1:
            return '1 minute'
        else:
            return f'{minutes} minutes'