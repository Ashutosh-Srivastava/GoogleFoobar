# This was my solution submitted and passed all the test cases
'''
@Author: Ashutosh Srivastava
Python3 solution
'''

def solution(l):
    answer=0
    if(len(l)<3):
        return answer
    else:
        for i in range(1,len(l)):
            a=len([a for a in l[:i] if l[i]%a==0])
            b=len([b for b in l[i+1:] if b%l[i]==0])
            answer+=a*b
        return answer
        
