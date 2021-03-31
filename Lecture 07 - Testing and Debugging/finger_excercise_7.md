## Consider the following function definition:

```py
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)
```
### When we call

> rem(2, 5)
### the shell returns 2. When we call

> rem(5, 5)
### the shell returns 0. But when we call

> rem(7, 5)
### the shell does not return anything! Using this information, choose what line of code should be changed from the following choices:


- [ ] if x == a:
- [ ] return 0
- [ ] elif x < a:
- [ ] return x
- [ ] else:
- [x] rem(x-a, a)

### How should this line be rewritten?

> return rem(x-a, a)
