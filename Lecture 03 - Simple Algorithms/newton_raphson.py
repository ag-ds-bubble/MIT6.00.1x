# Find square root using newton raphson
num = 987
eps = 1e-6
iteration = 0
sroot = num/2

while abs(sroot**2-num)>eps:
    iteration+=1
    if sroot**2==num:
        print(f'At Iteration {iteration} : Found It!, the cube root for {num} is {sroot}')
        break
    sroot = sroot - (sroot**2-num)/(2*sroot)
    print(f'At Iteration {iteration} : the square root approximation for {num} is {sroot}')
