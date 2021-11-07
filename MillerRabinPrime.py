import random

# Making A General GCD function
def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)


# 1. Picking a large random integer number. 
num = random.randint(1,10000)
while gcd(num,2310)!= 1:
    num = random.randint(1,10000)

print(num)

K = random.getrandbits(100)

print("K: "+ str(K)+" length:"+ str(len(str(K))))

X = 2310*K+num
def MillerRabinPrimalityTest(X):
    if(X>3):
        checkPrime(X)
    