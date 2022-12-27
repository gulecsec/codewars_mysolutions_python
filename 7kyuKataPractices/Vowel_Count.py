def get_count(sentence):
    return sum(i in 'aeiou' for i in sentence)
