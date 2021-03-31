### Consider the following Python procedures. For each one, specify its order of growth.
### Assume n has been previously bound to some value

```py
i = 0
while i < 5:
   n *= 2
   i += 1

print(n)
```
- [x] O(1)
- [ ] O(log(n))
- [ ] O(n)
- [ ] O(i)
- [ ] O(i log(n))
- [ ] O(n log(i))

```py
def iterPower(a, b):
   result = 1
   while b > 0:
      result *= a
      b -= 1
   return result
```
- [ ] O(1)
- [ ] O(log(a))
- [ ] O(log(b))
- [ ] O(a)
- [x] O(b)
- [ ] O(a*b)
- [ ] O(a^b)

```py
def recurPower(a, b):
   print(a, b)
   if b == 0:
      return 1
   else:
      return a * recurPower(a, b-1)
```
- [ ] O(1)
- [ ] O(log(a))
- [ ] O(log(b))
- [ ] O(a)
- [x] O(b)
- [ ] O(a*b)
- [ ] O(a^b)

```py
def recurPowerNew(a, b):
   print(a, b)
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)
```
- [ ] O(1)
- [ ] O(log(a))
- [x] O(log(b))
- [ ] O(a)
- [ ] O(b)
- [ ] O(a*b)
- [ ] O(a^b)