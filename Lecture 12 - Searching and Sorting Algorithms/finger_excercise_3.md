### Here is some code for linear search that uses the fact that a set of elements is sorted in increasing order:
```py
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

### Consider the following code, which is an alternative version of search.

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False
```

### Which of the following statements is correct? You may assume that each function is tested with a list L whose elements are sorted in increasing order; for simplicity, assume L is a list of positive integers.

- [x] search and search1 return the same answers.
- [ ] search and search1 return the same answers provided L is non-empty.
- [ ] search and search1 return the same answers provided L is non-empty and e is in L.
- [ ] search and search1 do not return the same answers.
- [ ] search and search1 return the same answers for lists of length 0 and 1 only.