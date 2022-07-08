import math


a = 1112
b = 695


def mod(a,b):
    return aget_ipython().run_line_magic("b", "")

def gcd(m,n):
    # 需要用大数除以小数，所以先判断哪个数字更大
    # 用递归一次直接把大数变成a小数变成b
    if m < n:
        return gcd(n,m)

    # 先判断第一次求余是否为0 如果为0则循环不继续 被除数n就是最大公约数
    remainder = mod(m,n)
    while remainder get_ipython().getoutput("= 0: # 如果余数不为0就继续循环除")
        m = n # 交换除数位置将原本的被除数放到除数的位置上
        n = remainder # 将上一次的余数变成除数
        remainder = mod(m,n) # 求余数

    return n

gcd(a,b)


def is_coprime(a,b):
    if a:
        if b:
            if gcd(a,b) ==1:
                return True
            else:
                return False
        return "b must not be equal to 0 "
    return "a must not be equal to 0 "

is_coprime(3,2)


def is_prime(n):
    if n > 1 :
        for i in range(2, (int(math.sqrt(n))+1) ):
            remainder = mod(n,i)
            if remainder == 0:
                return False
        return True
    return False

is_prime(2)


def is_composite(n):
    if n > 1:
        if is_prime(n):
            return False
        else:
            return True
    return False

is_composite(4)


def if_one_in_here(m,n):
    if m==1:
        return True
        if n==1:
            return True
    
if_one_in_here(1,2)


def reduceNum(n):
    print ('{} = '.format(n), end=" ")
    if not isinstance(n, int) or n <= 0 :
        print ('请输入一个正确的数字 get_ipython().getoutput("')")
        exit(0)
    elif n in [1] :
        print ('{}'.format(n))
    while n not in [1] : # 循环保证递归
        for index in range(2, n + 1) :
            if n % index == 0:
                n //= index # n 等于 n//index
                if n == 1: 
                    print (index )
                else : # index 一定是素数
                    print ('{} *'.format(index), end=" ")
                break
reduceNum(1)






