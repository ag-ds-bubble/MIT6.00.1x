### Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the result is a function, select function and write 'function' in the box.

### To get the most out of this problem, try to figure out the answers by reading the code, not running it. Run the code in your interpreter only after you've checked your answers a few times.

```py
>>> a = 10
>>> def f(x):
      return x + a
>>> a = 3
>>> f(1)
```

- [ ] NoneType
- [ ] num
- [x] int
- [ ] float
- [ ] boolean
- [ ] function

> 4

```py
>>> x = 12
>>> def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
>>> g(x)
```

- [ ] NoneType
- [ ] num
- [x] int
- [ ] float
- [ ] boolean
- [ ] function

> 19
 

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



### Q2) b(3, 2)



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



