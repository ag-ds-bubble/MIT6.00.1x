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

### If a given loop will not terminate, write the phrase 'infinite loop' (no quotes) in the box. Recall that you can stop an infinite loop in your program by typing CTRL+c in the console.

```py
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 
```
> 0, 1, 2, 3, 4, 5, Outside of loop, 6

```py
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
```
> infinite loop

```py
num = 10
while num > 3:
    num -= 1
    print(num) 
```
> 9, 8, 7, 6, 5, 4, 3


```py 
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
```
> 10, 9, 8, 7, Breaking out of loop, Outside of loop

### Note: If the command break is executed within a loop, it halts evaluation of the loop at that point and passes control to the next expression. Test some break statements inside different loops if you don't understand this concept!

```py
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 
```
> infinite loop