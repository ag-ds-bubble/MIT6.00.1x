### As we'll see in subsequent lectures, everything in Python is an object. Objects are special because we can associate special functions, referred to as object methods, with the object. In this problem you'll be working with string objects, and their built-in methods.
### A complete description of the methods available to string objects can be found in the Python library reference on string methods.
### In this exercise, we want you to get some experience in using methods as functions. The convention for object methods is to use the "dot" notation, so that if s is a string, evaluating s.upper will return the actual function, and evaluating s.upper() will cause the function itself to be evaluated (in this case it returns a new string, since strings are immutable) with every character now in upper case. An example of this follows:
```py
>>> s = 'abc'
>>> s.capitalize
<built-in method capitalize of str object at 0x104c35878>
>>> s.capitalize()
'Abc'
```

### For each of the expressions in this problem, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value. If it would be a function, select type 'function' and put the word 'function' in the box for the value.
### Assume we've made the following assignments:
```py
> str1 = 'exterminate!' 
> str2 = 'number one - the larch'
```
### Assume that the expressions are evaluated in the order shown - that is, each problem part is evaluated directly after the previous problem part(s).


### Q1) str1.upper

- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [x] function
- [ ] string

> function

### Q2) str1.upper()
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [x] string

> EXTERMINATE!

### Q3) str1
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [x] string

> exterminate!

### Q4) str1.isupper()
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [x] string

> False

### Q5) str1.islower()
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [x] function
- [x] string

> True

### Q6) str2 = str2.capitalize()
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [x] function
- [x] string

> Number one - the larch

### Q7) str2.swapcase()
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [x] string

> nUMBER ONE - THE LARCH

### Q8) str1.index('e')
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string

> 0

### Q9) str2.index('n')
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string

> 8

### Q10) str2.find('n')
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string

> 8

### Q11) str2.index('!')
- [x] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string

> error

### Q12) str2.find('!')
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string

> -1

### Q13) str1.count('e')
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string

> 3

### Q14) str1 = str1.replace('e', '*')
###     str1
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [x] string

> *xt*rminat*!

### Q15) str2.replace('one', 'seven')
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [x] string

> Number seven - the larch
