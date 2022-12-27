def sum_two_smallest_numbers(numbers):
    asc = sorted(numbers)
    for i in range(len(numbers)):
        if i < 1:
            return asc[i] + asc[i+1]
