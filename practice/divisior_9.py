# import math

# def find_prime(n):
#     prime = [True] * (n+1)
#     p = 2 
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p*p, n+1, p):  
#                 prime[i] = False
#         p += 1        
    
#     limit = int(math.sqrt(n))
#     res = []
#     for p in range(2, limit+1): 
#         if prime[p]:
#             res.append(p)    
    
#     ans = 0 
#     k = len(res)
    
#     for j in range(k):  
#         s = res[j]
#         if (s ** 8 <= n):
#             ans += 1
    
#     for x in range(k):  
#         for y in range(x+1, k):  
#             if (res[x]**2 * res[y]**2) <= n: 
#                 ans += 1
    
#     return ans       

# print(find_prime(100))
















import math

def countNumbers(n):
    if n< 36:
        return 0 
    c = 0
    limit = int(math.sqrt(n)) +1
    is_prime = [True] * (limit)

    prime = [i for i in range(limit + 1)]

    # Sieve to store smallest prime factor
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                if prime[j] == j:
                    prime[j] = i

    for i in range(2, limit + 1):
        p = prime[i]
        q = prime[i // prime[i]]

        # Check for p^2 * q^2 form
        if p * q == i and q != 1 and p != q:
            c += 1
        # Check for p^8 form
        elif prime[i] == i and pow(i, 8) <= n:
            c += 1

    return c

n = 100
print(countNumbers(n))