def jos(n: int, k: int) -> int:
    if n == 1:
        return 1
    else:
        return (jos(n - 1, k) + k-1) % n + 1 
            
        # RR 
        # (n-1, k) % n
        # positions are being shifted by k, so, 
        # in after killing a person pos of (k+1)th person is now 1th pos

jos(5,2)