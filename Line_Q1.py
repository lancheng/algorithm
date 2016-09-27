def fibonacci(n):
    if n <= 0:
        raise
    
    if n == 1:
        return 1
    
    '''
    1. use dynamic programming to resolve this problem. The recursive solution is very time-consuming
    when n is big.

    2. since python supports 'big int', we can use its built-in long type and standard math operations.
    otherwise, for example if we use C++ to resolve this poblem, we need to take advantages of other 
    libraries, like boost cpp_int, or implement our own big int type.
    '''
    dp = [0,1]
    
    for i in xrange(2, n + 1):
        dp[i % 2] = sum(dp)

    return dp[n % 2]

if __name__ == '__main__':
    import sys
    import time
    try:
        st = time.time()
        r = fibonacci(int(sys.argv[1]))
        print time.time() - st
        print r
    except:
        print 'Please input a positive integer.'
