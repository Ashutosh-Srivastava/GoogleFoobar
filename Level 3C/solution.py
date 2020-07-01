# This was my solution submitted and passed all the test cases
'''
@Author: Ashutosh Srivastava
Python3 solution
'''

def solution(x, y):
    answer=0
    x=int(x)
    y=int(y)
    while (x!=1 or y!=1):
        if (x==1 or y==1):
            if (x==1):
                return str(answer+(y-1))
            if (y==1):
                return str(answer+(x-1))
        if(x<y):
            if(x==0):
                return "impossible"
            answer+=y/x
            y%=x
        else:
            if(y==0):
                return "impossible"
            answer+=x/y
            x%=y
    return str(answer)
