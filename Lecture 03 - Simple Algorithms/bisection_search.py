# Find cure root using bisection search
num = 43
eps = 1e-6
iteration = 0
croot = num/2

_high = num
_low = 1

while abs(croot**3-num)>eps:
    iteration+=1
    cube = croot**3
    if cube==num:
        print(f'At Iteration {iteration} : Found It!, the cube root for {num} is {croot}')
        break
    elif cube>num:
        _high = croot
    elif cube<num:
        _low = croot
    print(f'At Iteration {iteration} : the cube root aproximation for {num} is {croot}')
    croot=(_high+_low)/2

