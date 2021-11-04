import random
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
n= random.randint(2,10000)

while gcd(n,2310)==1:
    n= random.randint(2,10000)

k = random.getrandbits(100)
x = 2310*k + n

def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    if k == 1 or gcd(n,k) >1:
        print("test fail")
        return False
    temp = n-1
    counter = 0
    while temp % 2 == 0:
        temp = temp//2
        counter+=1

    for p in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, temp, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(counter - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

n= random.randint(2,10000)

while gcd(n,2310)==1:
    n= random.randint(2,10000)

k = random.getrandbits(100)
x = 2310*k + n

while(miller_rabin(x,k) is False):
    k = random.getrandbits(100)
    x = 2310*k + n























