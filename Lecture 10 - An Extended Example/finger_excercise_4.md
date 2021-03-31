### This problem will ask a series of questions about generators.
### Q1) Thinking about the genPrimes generator from the last problem, which of the following can be done only by using a generator, instead of defining a function (that uses any type of construct we've learned about, except generators)?
- [ ] Return 1000000 prime numbers
- [ ] Print every 10th prime number, until you've printed 20 of them
- [ ] Keep printing the prime number until the user stops the program
- [x] Everything that can be done with generator can be done with a function

### Q2) Every procedure that has a yield statement is a generator.
- [x] True
- [ ] False

### Q3) If a procedure has only one yield statement, but that statement will never be executed, then the procedure is not a generator.
- [ ] True
- [x] False

### Q4) If we were to use a generator to iterate over a million numbers, how many numbers do we need to store in memory at once?
- [ ] 1
- [x] 2
- [ ] 1000
- [ ] 1000000
- [ ] Don't need to store anything in memory

### For the following tasks, would it be best to use a generator, a standard function, or either?
### Q5) Finding the nth Fibonacci number
- [ ] Generator
- [x] Standard function
- [ ] Either a generator or standard function is fine

### Q6) Printing out an unbounded sequence of Fibonacci numbers
- [x] Generator
- [ ] Standard function
- [ ] Either a generator or standard function is fine

### Q7) Printing out a bounded sequence of prime numbers, where the prime numbers are successively computed by division by smaller primes
- [ ] Generator
- [ ] Standard function
- [x] Either a generator or standard function is fine

### Q8) Printing out an unbounded sequence of prime numbers, where the prime numbers are successively computed by division by smaller primes
- [x] Generator
- [ ] Standard function
- [ ] Either a generator or standard function is fine

### Q9) Finding the score of a word from the 6.00x Word Game of Pset 4
- [ ] Generator
- [x] Standard function
- [ ] Either a generator or standard function is fine

### Q10) Iterating over a sequence of numbers in a random order, where no number is repeated
- [ ] Generator
- [x] Standard function
- [ ] Either a generator or standard function is fine
