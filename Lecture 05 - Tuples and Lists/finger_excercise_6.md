### Here is the code for a function applyToEach:

```py
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
```

### Assume that

```
testList = [1, -4, 8, -9]
```

### For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

****
```py
>>> print(testList)
  [1, 4, 8, 9]
```
```py
applyToEach(testList, abs)
```



****
```py
>>> print(testList)
  [2, -3, 9, -8]
```
```py
applyToEach(testList, lambda x: x+1)
```



****
```py
>>> print testList
  [1, 16, 64, 81]
```
```py
applyToEach(testList, lambda x: x**2)
```
