### In this problem you'll be given a chance to practice writing some while loops.

### 1. Convert the following into code that uses a while loop.

### prints 2
### prints 4
### prints 6
### prints 8
### prints 10
### prints Goodbye!

```py
num=0
while num<10:
    num+=2
    print(num)
print("Goodbye!")
```

### 2. Convert the following into code that uses a while loop.

### prints Hello!
### prints 10
### prints 8
### prints 6
### prints 4
### prints 2

```py
num=0
print("Hello!")
while num<10:
    print(10-num)
    num+=2
```

### 3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:

### 21, which is 1 + 2 + 3 + 4 + 5 + 6.

### For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will provide values so write your code in the following box assuming these variables are already defined.

```py
sum_=0
while end>0:
    sum_+=end
    end-=1
print(sum_)
```
