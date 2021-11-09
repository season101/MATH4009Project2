import random

# Making A General GCD function
def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)


# 1. Picking a large random integer number. 
n = random.randint(1,10000)
while gcd(n,2310)!= 1:
    n = random.randint(1,10000)

print("n: "+str(n))

K = random.getrandbits(100)
x = 2310*K + n

print("K: "+ str(K)+" length:"+ str(len(str(K))))
print("x: "+ str(x)+" length:"+ str(len(str(x))))

### 3. Miller Rabin's Primality Test

# Utility function to do modular exponentiation. It returns (a^b) % p . 
def power(a, b, p):     
    
    res = 1;  # Initialize result      
    
    # Update x if it is more than or equal to p 
    x = a % p;  

    while (b > 0):    
        # If y is odd, multiply x with result 
        if (b & 1): 
            res = (res * a) % p; 
  
        # y must be even now 
        b = b>>1; # y = y/2 
        a = (a * a) % p; 
      
    return res; 
  
# This function is called for all k trials. It returns false if n is composite and returns false if n is probably prime. d is an odd  
# number such that d*2<sup>r</sup> = n-1 for some r >= 1 
def miillerTest(d, n): 
      
    # Pick a random number in [2..n-2] Corner cases make sure that n > 4 
    a = 2 + random.randint(1, n - 4); 
  
    # Compute a^d % n 
    x = power(a, d, n); 
  
    if (x == 1 or x == n - 1): 
        return True; 
  
    # Keep squaring x while one  of the following doesn't happen 
        # (i) d does not reach n-1 
        # (ii) (x^2) % n is not 1 
        # (iii) (x^2) % n is not n-1 
    while (d != n - 1): 
        x = (x * x) % n; 
        d *= 2; 
  
        if (x == 1): 
            return False; 
        if (x == n - 1): 
            return True; 
  
    # Return composite 
    return False; 
  
# It returns false if n is composite and returns true if n is probably prime. k is an input parameter that determines accuracy level. 
# Higher value of k indicates more accuracy. 
def isPrime( n, k): 
      
    # Corner cases 
    if (n <= 1 or n == 4): 
        return False; 
    if (n <= 3): 
        return True; 
  
    # Find r such that n =  2^d * r + 1 for some r >= 1 
    d = n - 1; 
    while (d % 2 == 0): 
        d //= 2; 
  
    # Iterate given nber of 'k' times 
    for i in range(k): 
        if (miillerTest(d, n) == False): 
            return False; 
  
    return True; 
  
# Driver Code 
# Number of iterations  
flag = True
num = 1
while (flag): 
    if (isPrime(x, K)): 
        print("Iteration "+str(num)+": "+str(x) + " is prime", end=" "); 
        print("K: "+str(K))
        flag = False
        num+=1
    else:
        print ("Iteration "+str(num)+": "+str(x) + " is not prime")
        K = random.getrandbits(100)
        x = 2310*K + n
        num+=1