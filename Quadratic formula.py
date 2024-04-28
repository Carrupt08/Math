a = float(input('a= : '))
b = float(input('b= : '))
c = float(input('c= : '))
D = (b**2-4*a*c)**0.5
if D<0:
    print('There are no real number solutions.')
else:
    d_pos = (-b+D)/2*a
    d_neg = (-b+D)/2*a
    print('Solution 1: ', d_pos)
    print('Solution 2: ', d_neg)