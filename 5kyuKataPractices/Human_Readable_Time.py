def make_readable(seconds):
    HH = seconds // 3600
    MM = (seconds - HH * 3600) // 60
    SS = seconds - (HH * 3600) - (MM * 60)
    return f"{HH:0>2d}:{MM:0>2d}:{SS:0>2d}"
