# Square root algo - Hero of Alexandria
num = 16
eps= 1e-20
guess = 9
diff = abs(num-guess**2)
iteration = 0

while diff>eps:
    guess = (guess + (num/guess))/2
    diff = abs(num-guess**2)
    iteration+=1
    print(f'Iteration {iteration}, Guess Updated : {guess}, diff : {diff}')