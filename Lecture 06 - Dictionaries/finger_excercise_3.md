### Consider the following sequence of expressions:
```py
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
```

### We want to write some simple procedures that work on dictionaries to return information.

### This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

```py
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    bignum = 0.0
    bigkey = None
    for ek, ev in aDict.items():
        if len(ev)>bignum:
            bignum=len(ev)
            bigkey=ek
            
    return bigkey
```