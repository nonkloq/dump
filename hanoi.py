from os import system 
from time import sleep, time 

intro = """
Author: github.com/nonkloq (satz)
Tower of Hanoi Algorithm Visualization in Terminal using ASCII

Usage:
    Lock Frame to see animation (y), or see every frame separately (n), Default n.
    Set Frame Interval in seconds, Input type Floating Point Number (No Defaults).
    Number of Disks to be used, Input type Integer (No Default, Recommended range limit [1-10] no upper bound restriction)
    Custom Start to Destination, Input type Integer, Available Slots A(1),B(2) and C(3), Default A(1) to C(3).

    Quit, Default n, y to quit.
"""

class Colors:
    __FG = {"g1":30,"r":31,"b1":32,"b2":33,"p1":34,"b3":35,"b4":36,"w1":37,"g2":90,"o":91,"b5":92,"y":93,"b6":94,"p2":95,"b6":96,"w2":97,"n":0}
    __BG = {"g1":40,"r": 41,"b1":42,"b2":43,"p1":44,"b3":45,"b4":46,"w1":47,"g2":100,"o":101,"b5":102,"y":103,"b6":104,"p2":105,"b6":106,"w2":107,"n":0}
    __EFX = {
            "emb": 2,
            "bold" : 1, 
            "ital": 3,
            "undrln": 4,
            "undrln2": 52,
            "dundrln" :21,
            "blink": 5,
            "highl": 7,
            "strike": 9
            }

    __base = "\033["
    __endl = "\033[0m"
    
    def _get_base(self,num: int)->str:
        return self.__base+str(num)+"m"

    def apply_fx(self,string: str,fx: str)-> str:
        return self._get_base(self.__EFX[fx])+string+self.__endl

    def apply_color(self,string: str, fg: str = "n", bg: str = "n")->str:
        return self._get_base(self.__BG[bg])+self._get_base(self.__FG[fg])+string+self.__endl


class TowerofHanoi(Colors):

    def __init__(self,single_frame: bool =False, frame_interval: float =0)->None:
        self.single_frame = single_frame
        self.frame_interval = frame_interval
        self.N = 0
        self.empty = ""
        self.T = None
        self.rod_colors = ["b5","o","b6", "r"]
        self.base = "w2"

    def __pt(self)->None:
        for i in range(self.N-1,-1,-1):
            print(f" {self.T[0][i] if i < len(self.T[0]) else self.empty} {self.__color_bound('|')} {self.T[1][i] if i < len(self.T[1]) else self.empty} {self.__color_bound('|')} {self.T[2][i] if i < len(self.T[2]) else self.empty}")
        print(self.__color_bound("-"*(self.N*3+8)))

    def __pm(self, n: int, s: int , e: int)-> None: # Make move and print
        self.T[e-1].append(self.T[s-1].pop())      
        self.__pt()
        print(f"Disk {n}: {s} => {e}\n")

    # hanoi function
    def __hanoi(self, n: int, start: int, end: int)->None:
        if n == 1:
            if self.frame_interval >0: sleep(self.frame_interval)
            if self.single_frame: system(CLEAR)
            self.__pm(n,start,end)
            return
        aux = 6 - (start + end)
        self.__hanoi(n-1,start,aux)
        if self.frame_interval>0: sleep(self.frame_interval)
        if self.single_frame: system(CLEAR)
        self.__pm(n,start,end)
        self.__hanoi(n-1,aux,end)

    def __color_bound(self,string: str)->str:
        return self.apply_color(string,self.base,self.base)

    def __color_rod(self,n: int,string: str)->str:
        return self.apply_fx(self.apply_color(string,self.rod_colors[n%len(self.rod_colors)]),"bold")

    def __f(self,x: int)->int:
        if x == 1: return x
        return 1+2*self.__f(x-1)

    def __call__(self,N: int,a: int,b: int)->None:
        self.N = N
        if self.single_frame: system(CLEAR)
        self.T = [[],[],[]]
        for i in range(N,0,-1):
            s = N-i 
            self.T[a-1] += [" "*s+self.__color_rod(i,"="*i)]
        self.empty=" "*N 
        self.__pt()
        print("Rods filled with disks!\n")
        s = time()
        self.__hanoi(N,a,b)
        e = time()
        print(self.apply_fx("\nTotal Moves for "+str(N)+" disks: "+str(self.__f(N)),"bold"))
        print(self.apply_fx(f"Time taken to complete at {self.frame_interval}s Frame Interval: {e-s:.4f}s\n","bold"))
        

if __name__ == "__main__":
    from os import name 
    if name == "posix": CLEAR = "clear"
    else: CLEAR = "cls"
    print(intro)
    
    hanoi = TowerofHanoi()
    res = ""
    try:
        while res != "y":
            hanoi.single_frame = True if input("Lock in Single Frame?(y/[n]): ") == "y" else False 
            hanoi.frame_interval = float(input("Frame Interval: "))
            N = int(input("# of disks: "))
            if N<=0: 
                print("Invalid Number")
                exit(1)
            if input("Custom Start to Dest?(y/[n]): ") == "y": a,b = int(input("Start: ")),int(input("Dest: "))
            else: a,b = 1,3
            hanoi(N,a,b)
            res = input("wanna a Quit? (y/[n]): ")
            print()
    except KeyboardInterrupt:
           print("KeyboardInterrupt")
