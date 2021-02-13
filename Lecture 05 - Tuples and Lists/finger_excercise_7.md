### Here is a different piece of code for working with lists:

```py
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
```

### Suppose that you are given the following functions:

```py
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
```

### For each of the following questions, indicate what value is returned. If you believe that an error will occur, write the word 'error'.

****
```py
applyEachTo([inc, square, halve, abs], -3)
```

```py
[-2, 9, -1.5, 3]
```

****
```py
applyEachTo([inc, square, halve, abs], 3.0)
```

```py
[4.0, 9.0, 1.5, 3.0]
```


****
```py
applyEachTo([inc, max, int], -3)
```

```py
```
