def lovefunc( flower1, flower2 ):
    lov1 = flower1 %2
    lov2 = flower2 %2
    hope = sorted([lov1, lov2])
    return hope == [0,1]
