### Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the result is a function, select function and write 'function' in the box. As always, try to do this problem by hand before turning to your interpreter.

### Assume the following definitions have been made:

```py
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
 ```

### Q1) a(False, 2, 3)

- [ ] NoneType
- [ ] num
- [x] int
- [ ] float
- [ ] boolean
- [ ] function

> 3



### Q2) b(3, 2)

- [ ] NoneType
- [ ] num
- [x] int
- [ ] float
- [ ] boolean
- [ ] function

> 3



### Q3) a(3>2, a, b)

- [ ] NoneType
- [ ] num
- [ ] int
- [ ] float
- [ ] boolean
- [x] function

> function



### Q4) b(a, b)

- [x] NoneType
- [ ] num
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function

> error



