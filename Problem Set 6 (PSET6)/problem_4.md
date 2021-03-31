### Consider the following Python procedure. Specify its order of growth.

```py
def modten(n):
    return n%10
```
[x] O(1)
[ ] O(log(n))
[ ] O(n)
[ ] O(nlog(n))
[ ] O(n^2)


### Consider the following Python procedure. Specify its order of growth.
```py
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result   
```
[ ] O(1)
[ ] O(log(len(n)))
[x] O(len(n))
[ ] O(len(n) log(len(n)))
[ ] O(len(n)^2)



### Consider the following Python procedure. Specify its order of growth.
```py
def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1
```
[ ] O(1)
[ ] O(log(n))
[ ] O(n)
[ ] O(nlog(n))
[ ] O(n^2)
[ ] O(n^3)
[ ] O(2^n)
### WRONG ANSWER!


### Consider the following Python procedure. Specify its order of growth.
```py
def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)
```  
[ ] O(1)
[ ] O(log(n))
[x] O(n)
[ ] O(nlog(n))
[ ] O(n^2)
[ ] O(n^3)
[ ] O(2^n)


### Consider the following Python procedure. Specify its order of growth.
```py
def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )
```
[ ] O(1)
[ ] O(log(n))
[ ] O(n)
[ ] O(nlog(n))
[x] O(n^2)
[ ] O(n^3)
[ ] O(2^n)
