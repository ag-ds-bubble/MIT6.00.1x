## Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated inside the print. If evaluating an expression would cause an error, select NoneType and write error in the box. If the result is a function, select function and write function in the box. As always, try to do this problem by hand before turning to your interpreter for help.

## Assume the following definitions have been made:

```py
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
```
## Q1)
```py
w1 = Weird(X, Y)
print(w1.getX())
```
- [x] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
> error

## Q2)
```py
print(w1.getY())
```
- [x] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
> error

## Q3)
```py
w2 = Wild(X, Y)
print(w2.getX())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 7

## Q4)
```py
print(w2.getY())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 8

## Q5)
```py
w3 = Wild(17, 18)
print(w3.getX())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 17

## Q6)
```py
print(w3.getY())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 18

## Q7)
```py
w4 = Wild(X, 18)
print(w4.getX())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 7

## Q8)
```py
print(w4.getY())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 18

## Q9)
```py
X = w4.getX() + w3.getX() + w2.getX()
print(X)
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 31

## Q10)
```py
print(w4.getX())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 7

## Q11)
```py
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 44

## Q12)
```py
print(w2.getY())
```
- [ ] NoneType
- [x] int
- [ ] float
- [ ] boolean
- [ ] function
> 8
