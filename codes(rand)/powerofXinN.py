from sys import argv
n = int(argv[2])
x = int(argv[1])

def PowerOfXinN(n,x):
    power = 0
    if n < 0:
        return False, -1
    while n > 1 and n % x == 0:
        n = n // x
        power += 1
    return n == 1, power

if __name__ == "__main__":
    isPow, Pow = PowerOfXinN(n,x)
    if isPow:
        print(f"The Power of {x} in the number {n} is: {Pow}")
    else:
        print(f"There in no Power of {x} in this number {n}")
