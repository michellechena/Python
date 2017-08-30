def hailstone(n):
    nums = []
    nums.append(n)
    while n != 1:
        if n % 2 == 0: 
            n = n // 2
            nums.append(n)
        else:
            n = n * 3 +1 
            nums.append(n)
    for i in nums:
        print (i)
    print(len(nums))


hailstone(20)

def isprime(num):
    i = 2
    prime = True
    while i < num:
        if (num % i == 0):
           prime = False
           break
        i +=1
    return prime

def factor(num):
    nums=[]
    for i in range(1, num):
        if (num % i == 0):
            nums.append(i)
    if (isprime(num)):
        nums.append(num)
    return nums

print(factor(3))
print(factor(4))

def multiple(a, b):
    factor1=factor(a)
    factor2=factor(b)

    factor3 = list(set(factor1 + factor2))
    mult = 1
    for i in factor3:
       mult *= i
    return mult



def uniquedigits(num):
    digits = []
    while (num !=0):
        digits.append( num % 10)
        num = num //10
    return set(digits)

print(uniquedigits(11111))

print(uniquedigits(123455555))

print(uniquedigits(10000)) # 0 and 1

print(uniquedigits(101)) # 0 and 1
 
print(uniquedigits(10)) # 0 and 1