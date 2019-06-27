#python3
import numpy as np
def fibonacci(n):
    if(n==0):
        return 0
    F=np.matrix([[1,1],[1,0]])
    F=F**(n-1)
    return(F.item(0,0))

def main():
    n=int(input())#Enter the the number 
    print(fibonacci(n))
    
if __name__=='__main__':
    main()