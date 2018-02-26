import math
def quadratic(a,b,c):
    if (b*b-4*a*c) < 0:
        raise TypeError('false data')
    else:
        t = math.sqrt(b*b-4*a*c)
        x = (-b+t)/(2*a)
        y = (-b-t)/(2*a)
    return x,y

print(quadratic(1,-2,1))
print("hello")
