def spin_words(sentence):
    listo = sentence.split()
    string = ''
    if len(listo) < 2:
        if len(sentence) > 4:
            string += sentence[::-1]
        else:
            string += sentence
        return string
    else:
        string2 = []
        for i in range(len(listo)):
            if len(listo[i]) > 4:
                string2.append(listo[i][::-1])
            else:
                string2.append(listo[i])
        return " ".join(string2)
