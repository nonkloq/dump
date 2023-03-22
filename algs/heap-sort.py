
def heap_bottomup(H,n):
    for i in range(n//2,-1,-1):
        k = i 
        v = H[i]
        heap = False
        while not heap and 2*k<n: 
            j= 2*k+1
            if j < n and H[j] < H[j+1]: j+=1
            
            if v >= H[j]: heap = True
            else: 
                H[k] = H[j]
                k = j
        H[k] = v

def max_key_deletion(H,n):
    H[0],H[n] = H[n],H[0]
    n-=1
    heap_bottomup(H,n)
    return n

def heapsort(H):

    n = len(H)-1
    heap_bottomup(H,n) # heapify
    
    while n:
        n = max_key_deletion(H,n)
        

H = [2,9,7,6,5,8]

heapsort(H)
print("Sorted Array using Heap Sort Algorithm:",H)