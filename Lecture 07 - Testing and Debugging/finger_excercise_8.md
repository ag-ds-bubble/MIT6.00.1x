## Consider the following function definition:

```py
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)
```
### When we call

> f(3)
### we expect the result 6, but we get 0.

> rem(5, 5)
### we expect the result 6, but we get 0.

> rem(7, 5)
### we expect the result 6, but we get 0.

### Using this information, choose what line of code should be changed from the following choices:

- [ ] if n == 0:
- [x] return n
- [ ] else
- [ ] return n * f(n-1)

### How should this line be rewritten?

> return 1
