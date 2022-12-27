def wave(people):

    check=[]
    for i, c in enumerate(people[:]):
        if people[i] == " ":
            pass
        else:
            up=people[i].upper()
            c=people[:i] + up + people[i+1:]
            check.append(c)

    print(check)

    return check
