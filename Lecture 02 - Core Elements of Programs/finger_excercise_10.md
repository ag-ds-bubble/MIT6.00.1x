### Below are some short Python programs. For each program, answer the associated questions.

### Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong. You'll learn the most this way, by figuring things out, instead of just running the code and reading off the answers.

```py
myStr = '6.00x'
for char in myStr:
    print(char)

print('done')
```

### Q) How many times does 6 print out?
>1

### Q) How many times does . print out?
>1

### Q) How many times does 0 print out?
>2

### Q) How many times does x print out?
>1

### Q) How many times does done print out?
>1


```py
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
```


### Q) How many times does H print out?
>1

### Q) How many times does e print out? Disregard the letters in the word done.
>2

### Q) How many times does l print out?
>3

### Q) How many times does o print out? Disregard the letters in the word done.
>1

### Q) How many times does ! print out?
>2

### Q) How many times does done print out?
>1


```py
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
```

### Q) How many times does o print out? Disregard the o's in last two print statements.
>0

### Q) How many times does M print out?
>1

### Q) What will the value of the variable numVowels be?
>11

### Q) What will the value of the variable numCons be?
>-25