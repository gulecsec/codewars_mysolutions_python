def grabscrab(said, possible_words):

    meaning = sorted(said)
    result = []
    for i in range(len(possible_words)):
        if len(sorted(possible_words[i])) != len(meaning):
            pass
        elif sorted(possible_words[i]) == meaning:
                result.append(possible_words[i])

    print(result)
    return result
