### Below are some short Python programs. For each program, answer the associated question.
### Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.
### This question is going to ask you what some simple loops print out. If you're asked what code like this prints:

```py
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)
```
### write what it prints out, separating what appears on a new line by a comma and a space. So the answer for the above code would be:

> 5, 4

### If a given loop will not terminate, write the phrase 'infinite loop' in the box.


```py
num = 10
for num in range(5):
    print(num)
print(num)
```
> 0, 1, 2, 3, 4, 4

```py
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
```
> 0.0, 1.0, 2.0, 3.0, 4.0

```py
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
```
> 0, Foo!, 4, 8, 12, 16, Foo!

```py
for letter in 'hola':
    print(letter)  
```
> h, o, l, a

```py
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
```
> Letter # 0 is S, 1
