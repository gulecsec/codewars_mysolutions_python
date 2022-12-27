def duplicate_encode(word):

    wordie = word.lower()

    result = ""
    for i in wordie:
        if wordie.count(i) > 1:

            result += ")"
        else:
            result += "("
    return result
