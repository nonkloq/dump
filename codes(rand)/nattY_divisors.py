from time import time
from sys import argv

class SeiveND:
    def __init__(self)->None:
        self.seive = [0,0]
        self.n = 2

    def update_seive(self,n: int) -> None:
        self.seive = [0]*(n+1)
        for i in range(2,n+1):
            if self.seive[i] == 0:
                self.seive[i] = i 
                for j in range(i*i,n+1,i):
                    self.seive[j] = i
        self.n = n

    def get_prime_divisors(self,n: int) -> list[int]:
        prime_divisors = []
        while n>1:
            p = self.seive[n]
            n //=p 
            prime_divisors.append(p)
        return prime_divisors

    def get_divisor(self,nums: list[int],powers: list[int]) -> list[int]:
        divisor = 1
        for i in range(len(nums)):
            divisor *= (nums[i]**powers[i])
        return divisor

    def get_divisors(self,n: int) -> list[int]:
        prime_divisors = self.get_prime_divisors(n)
        power_limit = {}
        nums = []
        for num in prime_divisors:
            if power_limit.get(num): power_limit[num]+=1
            else: 
                power_limit[num] = 1
                nums.append(num)
        n = len(nums)
        powers = [0]*n
        i= 0
        divisors = []
        while True:
            divisors.append(self.get_divisor(nums,powers))
            if powers[i]<power_limit[nums[i]]: powers[i]+=1
            else:
                while i<n and powers[i]>=power_limit[nums[i]]:
                    powers[i] = 0
                    i+=1
                if i<n: powers[i]+=1
                else: break
                i=0
        return divisors
    
    def __call__(self,n: int) -> list[int]:
        if n>self.n: self.update_seive(n)
        return self.get_divisors(n)


def get_divisors_n(n: int) -> list[int]:
    divisors = []
    for i in range(1,n+1):
        if n%i == 0: divisors.append(i)
    return divisors
def main() -> None:
    nlogn = SeiveND()
    try: 
        while True:
            n = int(input("Enter n: "))
            s = time()
            print("Naive: ",get_divisors_n(n))
            e = time()
            print(f"Time: {e-s}ms\n")
            s = time() 
            print("SeiveND: ",nlogn(n))
            e = time()
            print(f"Time: {e-s}ms\n")
    except:
        pass
if __name__ == "__main__":
    main()
