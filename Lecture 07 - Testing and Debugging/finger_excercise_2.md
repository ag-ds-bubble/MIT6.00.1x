## Consider the following code specification:

```py
def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
```

### Indicate which of the conditions below would combine to make a good black box test suite for the function union by selecting the appropriate choice(s).

- [x] set1 is an empty set; set2 is an empty set
- [x] set1 is an empty set; set2 is of size greater than or equal to 1
- [x] set1 is of size greater than or equal to 1; set2 is an empty set
- [x] set1 and set2 are both nonempty sets which do not contain any objects in common
- [x] set1 and set2 are both nonempty sets which contain objects in common