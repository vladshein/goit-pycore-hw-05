#HW5_task1

#define outer function for caching
def caching_fibonacci():

    cache = {}

    #define inner function, that will store state of cache dictionary
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        #make recursive calls to process next numbers        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    #return inner function
    return fibonacci

#test data
fib = caching_fibonacci()

print(fib(10))
print(fib(15))