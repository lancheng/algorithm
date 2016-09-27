'''
1. use DP
2. dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-4]+ dp[n-5] + dp[n-6], where n >= 6
3. since python supports 'big int', we can use its built-in long type and standard math operations. Otherwise, for example if we use C++ to resolve this poblem, we need to take advantages of other libraries, like boost cpp_int, or implement our own big int type.
'''
def dice_game(n):
    if n <= 0:
        raise
    
    result = [0] * 6
    result[0] = 1
    result[1] = 1

    for i in xrange(2, n + 1):
        result[i % 6] = sum(result)

    return result[n % 6]

if __name__ == '__main__':
    import sys
    import time
    try:
       st = time.time()
       
       r = dice_game(int(sys.argv[1]))
       print time.time() - st
       print r
    except:
        print 'Please input a number which is greater than 0'
