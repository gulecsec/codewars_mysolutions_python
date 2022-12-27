def make_password(phrase):
    i_I = "iI"
    o_O ="oO"
    s_S = "sS"
    password = ""
    phr = phrase.split(" ")
    for i in range(len(phr)):
        if any(d == phr[i][0] for d in i_I) == True:
            password += '1'
        elif any(e == phr[i][0] for e in o_O) == True:
            password += '0'
        elif any(f == phr[i][0] for f in s_S) == True:
            password += '5'
        else:
            password += phr[i][0]
        
    return(password)
