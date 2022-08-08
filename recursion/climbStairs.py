# tle on leetcode
# concept is fine

def climbStairs(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return climbStairs(n-1) + climbStairs(n-2)

 
        # to reach nth stair we can either come from 
        # (n-1)th stair or (n-2)th stair
        # RR
        # f(n) = f(n-1) + f(n-2)
        
        #basecase
        # if there is only one stair which is 0th then,
        # no of possible ways is 1
        
        # if there is less than one stair which is -ve then,
        # no of possible ways is 0
