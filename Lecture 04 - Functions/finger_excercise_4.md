### You have the following function definitions:

```py
def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  

```
    
Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the value of an expression is a function, select function as the type and write 'function' in the box.

### Q1) a(6)

- [ ] NoneType
- [ ] num
- [x] int
- [ ] float
- [ ] boolean
- [ ] function

> 7

### Q2) a(-5.3)

- [ ] NoneType
- [ ] num
- [ ] int
- [x] float
- [ ] boolean
- [ ] function

> -4.3


### Q3) a(a(a(6)))

- [ ] NoneType
- [ ] num
- [x] int
- [ ] float
- [ ] boolean
- [ ] function

> 9


### Q4) c(a(1), b(1))

- [ ] NoneType
- [ ] num
- [ ] int
- [x] float
- [ ] boolean
- [ ] function

> 4.0


### Q5) d('apple', 11.1)

- [x] NoneType
- [ ] num
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function

> error


### Q6) e(a(3), b(4), c(3, 4))

- [ ] NoneType
- [ ] num
- [ ] int
- [ ] float
- [x] boolean
- [ ] function

> False


### Q7) f

- [ ] NoneType
- [ ] num
- [ ] int
- [ ] float
- [ ] boolean
- [x] function

> function

