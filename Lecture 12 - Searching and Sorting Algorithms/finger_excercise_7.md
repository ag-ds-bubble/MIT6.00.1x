### This problem will walk through some applications of complexity analysis. Suppose you're asked to implement an application. One of the things it has to do is to report whether or not an item, x, is in a list L. L's contents do not change over time. Below are two possible ways to implement this functionality. Assume that mergeSort is implemented as per the lecture.

### L is a list with n items.

### Application A:
### Every time it's asked to, it performs a linear search through list L to find whether it contains x.

### Application B:
### Sort list L once before doing anything else (using mergeSort). Whenever it's asked to find x in L, it performs a binary search on L.

### Q1) If the application is asked to find x in L exactly one time, what is the worst case time complexity for Application A?
- [ ] O(1)
- [ ] O(logn)
- [x] O(n)
- [ ] O(nlogn)
- [ ] O(n2)

### Q2) If the application is asked to find x in L exactly one time, what is the worst case time complexity for Application B?
- [ ] O(1)
- [ ] O(logn)
- [ ] O(n)
- [x] O(nlogn)
- [ ] O(n2)

### Q3) If the application is asked to find x in L k times, what is the worst case time complexity for Application A?
- [ ] O(1)
- [ ] O(k+logn)
- [ ] O(k+n)
- [x] O(kn)
- [ ] O(n+klogn)

### Q4) If the application is asked to find x in L k times, what is the worst case time complexity for Application B?
- [ ] O(kn)
- [ ] O(nlogn)
- [ ] O(n+klogn)
- [x] O(nlogn+klogn)
- [ ] O(knlogn+logn)

### Q5) What value(s) of k would make Application A be faster (i.e., asymptotically grow slower than) Application B?
- [x] k=1
- [ ] k=n
- [ ] k=logn
- [ ] k=n2
- [ ] k=2n

### Q6) What value(s) of k would make Application A grow at the same rate as Application B?
- [ ] k=1
- [ ] k=n
- [x] k=logn
- [ ] k=n2
- [ ] k=2n

### Q7) Which application should you choose if you know that there are going to be n3 requests to find x in L?
- [ ] Application A
- [x] Application B

