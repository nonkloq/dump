import heapq as hq
from collections import Counter

class Node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    
    def __lt__(self,right):
        return self.freq < right.freq


def huffmantree(string):
    c = Counter(string)
    Q = []
    for key,val in c.items():
        hq.heappush(Q,Node(val,key))

    while len(Q)>1:
        left = hq.heappop(Q)  
        right = hq.heappop(Q)
        hq.heappush(Q, Node(left.freq+right.freq,None,left,right))
    
    return Q[0]

def extractcodes(tree):
    codes = {}
    def preorder(node,code):
        if node.symbol:
            codes[node.symbol] = code
            return 
        preorder(node.left,code+"0")
        preorder(node.right,code+"1")
    preorder(tree,"")
    return codes

def encode(string,codes):
    encoded_text = ""
    for x in string:
        encoded_text += codes[x]
    return encoded_text

def decode(string,tree):
    decoded_text = ""
    node = tree
    for x in string:
        if node.symbol:
            decoded_text += node.symbol
            node = tree
        if x == "1": node = node.right
        else: node = node.left
    return decoded_text


string = """
[Chorus]
Yeah, you know me, I'm the biggest bird (Uh)
Droppin' bars just like you've never heard (Uh)
Yeah, you better go and spread the word
But you should speak it like you mean it, you fuckin' nerd

[Post-Chorus]
'Cause I'm the biggest bird, I'm the biggest bird
I'm the biggest bird, I'm the biggest bird
I'm the biggest bird, I'm the biggest bird
I'm the biggest bird, I'm the biggest bird
"""

tree = huffmantree(string)
codes = extractcodes(tree)
encoded_text = encode(string,codes)
decoded_text = decode(encoded_text,tree)

print("Code Words: \n",codes)
print("\nEnconded Text:")
print(encoded_text)
print("\nDecoded Text:")
print(decoded_text)