### Consider the following code:

```py
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
```

### If this code is executed, it will print succeeded: 4.9999999999998 (or succeeded: 5.0). Remember floating point errors?

### Now suppose we try the following:

```py
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
```

### Select the answer that best describes what occurs when the above code is executed:

- [ ] Script successfully completes, and prints out succeeded: 4.9999999999998 (or succeeded: 5.0)
- [ ] Script successfully completes, but prints out failed
- [ ] Script successfully completes, but prints out succeeded: followed by some number not really close to 5.0
- [x] Script enters an infinite loop and never terminates


### Now suppose we try

```py
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
```

### Select the answer that best describes what occurs when the above code is executed:

- [x] Script successfully completes, and prints out succeeded: 4.9999999999998 (or succeeded: 5.0)
- [ ] Script successfully completes, but prints out failed
- [ ] Script successfully completes, but prints out succeeded: followed by some number not really close to 5.0
- [ ] Script enters an infinite loop and never terminates


### Finally, let's use the same code as immediately above, but change the first line to x = 23. Note that the square root of 23 is roughly 4.7958.
### Select the answer that best describes what occurs when the modified code is executed:

- [ ] Script successfully completes, and prints out succeeded: 4.9999999999998 (or succeeded: 5.0)
- [x] Script successfully completes, but prints out failed
- [ ] Script successfully completes, but prints out succeeded: followed by some number not really close to 5.0
- [ ] Script enters an infinite loop and never terminates

