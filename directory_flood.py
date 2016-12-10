import os
def rec(path,n):
    if(n==0):
        return
    for i in range(4):
        #createdir
        os.makedirs(path+'/'+'ABCD'[i])
        rec(path+'/'+'ABCD'[i],n-1)

rec('./virustrial',5)
