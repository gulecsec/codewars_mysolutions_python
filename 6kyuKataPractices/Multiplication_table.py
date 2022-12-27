def multiplication_table(size):

    i_th = list()
    for i in range(1, size+1):
        j_th = list()
        for j in range(1, size+1):
            j_th.append(i * j)
        i_th.append(j_th)
        
    print(i_th)
    return i_th
