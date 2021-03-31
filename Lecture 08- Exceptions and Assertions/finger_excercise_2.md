### Write what it prints out, separating what appears on a new line by a comma and a space.

```py
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
```

### What does fancy_divide([0, 2, 4], 1) print out?
> 1, 0

### What does fancy_divide([0, 2, 4], 4) print out?
> -1, 0

### What does fancy_divide([0, 2, 4], 0) print out?
> 0, "error"

### def fancy_divide(numbers, index):
```py
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
```

### What does fancy_divide([0, 2, 4], 1) print out?
> 1, 0

### What does fancy_divide([0, 2, 4], 4) print out?
> 1, 0, 0

### What does fancy_divide([0, 2, 4], 0) print out?
> -2, 0

```py
def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
```

### What does fancy_divide([0, 2, 4], 1) print out?
> 1, 0

### What does fancy_divide([0, 2, 4], 4) print out?
> 1, 0, 0

### What does fancy_divide([0, 2, 4], 0) print out?
> 0, -2

### def fancy_divide(list_of_numbers, index):
```py
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
```

### Does this code print 0 when you call fancy_divide([0, 2, 4], 0)?

[ ] Yes.
[x] No.

```py
def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
```

### Does this print 0 when you call fancy_divide([0, 2, 4], 0)?

[x] Yes.
[ ] No.