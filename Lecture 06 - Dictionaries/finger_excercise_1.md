### Suppose we evaluate the following expressions:

```py
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
```

### We are now going to evaluate a set of expressions, resulting in the following sequence of interactions. Fill in each blank to show what the Python interpreter would print at that point. If an expression below would generate an error, enter 'error'.

### Q1) >>> animals
>{'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}

### Q1) >>> animals['c']
>coati

### Q1) >>> animals['donkey']
>error

### Q1) >>> len(animals)
>4

### Q1) >>> animals['a'] = 'anteater'
###     >>> animals['a']
>anteater

### Q1) >>> len(animals['a'])
>8

### Q1) >>> 'baboon' in animals
>False

### Q1) >>> 'donkey' in animals.values()
>True

### Q1) >>> 'b' in animals
>True

### Q1) >>> animals.keys()
>dict_keys(['a', 'b', 'c', 'd'])

### Q1) >>> del animals['b']
###     >>> len(animals)
>3

### Q1) >>> animals.values()
>dict_values(['anteater', 'coati', 'donkey'])
