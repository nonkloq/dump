def binsearch(arr,key):
    """Binary Search O(log2 N)"""
    if not arr: return False

    mid = len(arr)//2
    if arr[mid] == key: return True
    
    if arr[mid]<key: return binsearch(arr[mid+1:],key)
    return binsearch(arr[:mid],key)

def fact(n):
    """Factorial O(N)"""
    if n<=1: return 1
    return fact(n-1)*n

def fib(n):
    """Fibonacci Series O(2^n)"""
    if n<=1: return n
    return fib(n-1) + fib(n-2)


def permute(data, i, length):
    """Permutaion nPr O(n!)"""
    if i==length:
        print(data)
    else:
        for j in range(i,length):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]

data = [1, 2, 3]
print(binsearch(data,3))
print(fact(8))
print(fib(12))
permute(data, 0, len(data))
