### Below are some short Python programs. For each program, answer the associated questions.
### Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

```py
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
```

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 0?
> 12

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 1?
> 24

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 2?
> 36

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 3?
> 48

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 4?
> 60


```py
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
```

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 0?
> 12

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 1?
> 12

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 2?
> 12

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 3?
> 12

### Q) What is the value of the variable count that is printed out (at the print statement) on iteration 4?
> 12


```py
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
```

### Q) How many times will the print statement be executed?
> 5

### Q) What is the largest value of the variable iteration that will be printed out (at the print statement)?
> 4

### Q) What is the largest value of the variable count that will be printed out (at the print statement)?
> 12

### Q) What is the smallest value of the variable count that will be printed out (at the print statement)?
> 1
