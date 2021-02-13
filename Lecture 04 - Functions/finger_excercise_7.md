### Enter the value of the expressions below.
### To get the most out of this problem, try to figure out the answers by reading the code, not running it. Run the code only after you've used up a few of your checks.

```py
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
     
foo(3)
```
> 11


```py
def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)
```
> 1

```py
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)
```
> 5

```py
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
```
> 3