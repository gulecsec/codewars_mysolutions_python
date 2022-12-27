def duplicate_count(text):
    if len(text) == 0:
        return 0
    duplicates=[]
    texto = text.lower()
    for i in texto:
        if texto.count(i) > 1:
            duplicates.append(i)
        elif texto.count == 1:
            continue

    print(len(set(duplicates)))
    return len(set(duplicates))
