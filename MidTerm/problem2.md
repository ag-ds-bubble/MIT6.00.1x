# Mid Term

## Problem 2-1
### Consider the statement: `L = {'1':1, '2':2, '3':3}`. Which is correct?

- [ ] L is a list
- [ ] L is immutable
- [ ] L contains 6 elements
- [ ] L has integer keys
- [x] L maps strings to integers


## Problem 2-2
### Assume a `break` statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?

- [ ] The program might immediately terminate.
- [ ] The function might immediately terminate.
- [x] The loop will always immediately terminate. (wrong)
- [ ] All of the above.
- [ ] None of the above.



## Problem 2-3
### In Python, which of the following is a mutable object?

- [ ] a string
- [ ] a tuple
- [x] a list
- [ ] all of the above
- [ ] none of the above



## Problem 2-4
### Assume the statement `s[1024] = 3` does not produce an error message. This implies:

- [ ] type(s) can be str
- [ ] type(s) can be tuple
- [ ] type(s) can be list
- [ ] All of the above


## Problem 2-5
### Consider the code:
```py
L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3
```
### Which of the following does NOT cause an exception to be thrown?
- [ ] print(L[3])
- [ ] print(d['b'])
- [x] for i in range(1000001, -1, -2): print(f)
- [ ] print(int('abc'))
- [ ] None of the above




## Problem 2-6
### Examine the following code snippet:
```py
stuff  = _____
for thing in stuff:
    if thing == 'iQ':
        print("Found it")
```
### Select all the values of the variable "stuff" that will make the code print "Found it".

- [x] ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
- [x] ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
- [ ] [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
- [ ] ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
- [x] ["iQ"]
- [ ] "iQ"


## Problem 2-7
### The following Python code is supposed to compute the square of an integer by using successive additions.
```py
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
```
### Not considering recursion depth limitations, what is wrong with this implementation of procedure Square? Check all that apply.
*Wrong*
- [ ] It is going to return a wrong value.
- [ ] The term Square is a reserved Python keyword.
- [x] Function names cannot start with a capital letter.
- [ ] The function is never going to return anything.
- [ ] Python has arbitrary precision arithmetic.
- [ ] This function will not work for negative numbers.
- [ ] The call SquareHelper(abs(x), abs(x)) won't work because you can't have abs(x) as both parameters.
- [x] Nothing is wrong; the code is fine as-is.
