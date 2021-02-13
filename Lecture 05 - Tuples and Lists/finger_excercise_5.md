### For the last expression in each question below, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value.

```py
>>> aList = [0, 1, 2, 3, 4, 5]
>>> bList = aList
>>> aList[2] = 'hello'
>>> aList == bList
```

- [ ] NoneType
- [ ] int
- [ ] float
- [x] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [ ] list
>True

```py
>>> aList is bList
```
- [ ] NoneType
- [ ] int
- [ ] float
- [x] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [ ] list
>True

```py
>>> aList
```
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [x] list
>[0, 1, 'hello', 3, 4, 5]

```py
>>> bList
```
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [x] list
>[0, 1, 'hello', 3, 4, 5]

```py
>>> cList = [6, 5, 4, 3, 2]
>>> dList = []
>>> for num in cList:
        dList.append(num)
>>> cList == dList
```
- [ ] NoneType
- [ ] int
- [ ] float
- [x] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [ ] list
>True

```py
>>> cList is dList
```
- [ ] NoneType
- [ ] int
- [ ] float
- [x] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [ ] list
>False

```py
>>> cList[2] = 20
>>> cList
```
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [x] list
>[6, 5, 20, 3, 2]

```py
>>> dList
```
- [ ] NoneType
- [ ] int
- [ ] float
- [ ] boolean
- [ ] function
- [ ] string
- [ ] tuple
- [x] list
>[6, 5, 4, 3, 2]
