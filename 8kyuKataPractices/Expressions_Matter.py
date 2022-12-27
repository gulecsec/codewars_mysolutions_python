def expression_matter(a, b, c):
    
    num1 = a * (b + c)
    num2 = a * b * c
    num3 = a + b * c
    num4 = (a + b) * c 
    num5 = a + b + c
    print(max( num1, num2, num3, num4, num5))
    return max( num1, num2, num3, num4, num5)
