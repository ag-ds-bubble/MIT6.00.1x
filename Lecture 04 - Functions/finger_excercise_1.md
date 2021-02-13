### For each of the following functions, specify the type of its return. You can assume each function is called with an appropriate argument, as specified by its docstring.
### If the output can be either an int or a float, select num, which isn't a real Python type, but which we'll use to ### Q) Indicate that either basic numeric type is legal.
### In fact, in Python, booleans True and False can be operated on as if they were the integers 1 and 0; but it is ugly and confusing to take advantage of this fact, and we will resolutely pretend that it isn't true.

### What are those lines under the function definitions?
```py
def a(x):
   '''
   x: int or float.
   '''
   return x + 1
```
### Q1) Indicate the type of the output that the function a will yield.

- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [x] num

```py
def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
```

### Q2) Indicate the type of the output that the function b will yield.

- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [x] num


```py
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y
```

- [ ] NoneType
- [ ] int
- [x] float
- [ ] boolean
- [ ] num
 
### Q3) Indicate the type of the output that the function c will yield.

- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [x] num



```py
def d(x, y):
   '''
   x: Can be int or float.
   y: Can be int or float.
   '''
   return x > y
```
 
### Q4) Indicate the type of the output that the function d will yield.

- [ ] NoneType
- [ ] int
- [ ] float
- [x] boolean
- [ ] num


```py
def e(x, y, z):
   '''
   x: Can be int or float.
   y: Can be int or float.
   z: Can be int or float.
   '''
   return x >= y and x <= z
```
 
### Q5) Indicate the type of the output that the function e will yield.

- [ ] NoneType
- [ ] int
- [ ] float
- [x] boolean
- [ ] num


```py
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
```

### Q6) Indicate the type of the output that the function f will yield.

- [x] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] num
