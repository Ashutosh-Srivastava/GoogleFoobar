# This was my solution submitted and passed all the test cases
'''
Author: Ashutosh Srivastava
Python3 solution
'''

def solution(s):
  res=""
  for i in s:
    if(i.islower()):
      res+=chr(97+(122-ord(i)))
    else:
      res+=i
  return res
      
