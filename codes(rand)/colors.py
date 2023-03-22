from random import choice
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
    
    def get_rand_clr(self)->str:
        return choice(list(self.__FG.keys())[:-1])
    
    def apply_random_fg(self,string: str)->str: 
        return self.apply_color(string,choice(list(self.__FG.keys())))

    def apply_fx(self,string: str,fx: str)-> str:
        return self._get_base(self.__EFX[fx])+string+self.__endl

    def apply_color(self,string: str, fg: str = "n", bg: str = "n")->str:
        return self._get_base(self.__BG[bg])+self._get_base(self.__FG[fg])+string+self.__endl

class ColoredNums:
    PRE = {'0': "\033[90m",'1': "\033[97m",'2':"\033[94m",'3':"\033[93m",'4':"\033[92m",'5': "\033[91m",'6':  "\033[31m",'7': "\033[96m" ,'8': "\033[36m" ,'9': "\033[95m"}
    END = "\033[0m"

    def __colorit(self,n):
        return self.PRE[n]+n+self.END
    
    def __call__(self,n):
        out = ""
        for x in str(n):
            out+= self.__colorit(x)
        return out


if __name__ == "__main__":
    c = ColoredNums()
    print(c(1234567890))
