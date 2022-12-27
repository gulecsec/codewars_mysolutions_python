def distances_from_average(test_list):
    
    total = 0
    for i in test_list:
        total += i
        
    avg = total/(len(test_list))
    
    a = map(lambda x: round(avg-x,2), test_list)
    return list(a)
