def is_flush(cards):
    for i in range(len(cards)-1):
        if cards[i][-1] != cards[i+1][-1]:
            return False
    return True
