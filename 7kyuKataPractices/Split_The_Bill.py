from statistics import mean
group = {'A': 20,'B': 15,'C': 10}
def split_the_bill(group):
    keys = list(group.values())
    keys2 = list(group.keys())
    average = abs(mean(keys))
    keys3 = [(round(i-average, 2)) for i in keys]
    rem = dict(zip(keys2, keys3))
    return rem

