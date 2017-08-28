def largest_factor(n):
    factors=[]
    for i in range(2,n):
       if (n % i == 0):
        factors.append(i)
    return max(factors)


def testreversee(alist):
    for i in range(0, len(alist)//2):
        pairIndex = len(alist) -i -1
        temp = alist[pairIndex]
        alist[pairIndex] = alist[i]
        alist[i] = temp
    return alist


def testreversee1(alist):
    left = 0
    right = len(alist) - 1
    while left < right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1
    return alist



nums = [1, 2, 4, 5, 6]
nums2 = nums[::-1]
print(nums2)

def reverse1(nums):
    nums1 =[]
    for i in list(reversed(nums)):
        nums1.append(i)
    return nums1

res = reverse1(nums2)
print(res)
testreversee(nums)
print(nums)

def reverse(a):
    midpoint = len(a)/2
    for item in a[:midpoint]:
        otherside = (len(a) - a.index(item)) - 1
        temp = a[otherside]
        a[otherside] = a[a.index(item)]
        a[a.index(item)] = temp
    return a

def rev_list1(l):
    return l[::-1]

def rev_list2(l):
    return list(reversed(l))

def rev_list3(l):
    l.reverse()
    return l

l = [1,2,3,4,5,6]; nl=[]
def rev_list4(l):
   nl=[]
   while l:
        x = l.pop()
        print(x)
        nl.append(x) 
        print
   return nl
   
rev_list4(l)