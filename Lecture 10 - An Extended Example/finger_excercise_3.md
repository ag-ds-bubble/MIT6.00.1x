### Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

```py
def isPrime(num):
    if num==2: return True
    _isprime_flag = True
    for i in range(2,int(num/2)+1):
        if num%i==0:
            _isprime_flag=False
            break
    return _isprime_flag

def genPrimes():
    prime = 1
    while True:
        prime+=1
        if isPrime(prime):
            yield prime
```