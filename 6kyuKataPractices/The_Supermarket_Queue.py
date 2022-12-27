def queue_time(customers, n):
    if not customers:
        return False
    if n >= len(customers):
        return max(customers)
    till = [0] * n
    for i in customers:
        till.sort()
        till[0] += i
    return max(till)