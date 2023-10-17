def check_prime(n):
    if n<=1:
        return False
    for i in range (2,int(n/2)+1):
        if n%i==0:
            return False
    return True

def prime_numbers(list):
    prime_num=[]
    for i in list:
        if check_prime(i):
            prime_num.append(i)
    return prime_num

list=[1,2,3,4,5,6,7,8,9,10,11]
print(prime_numbers(list))