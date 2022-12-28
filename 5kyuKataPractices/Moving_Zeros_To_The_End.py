def move_zeros(lst):
    zeros = []
    others = []
    for num in lst:
        if num == 0:
            zeros.append(num)
        else:
            others.append(num)
    others.extend(zeros)
    return others
