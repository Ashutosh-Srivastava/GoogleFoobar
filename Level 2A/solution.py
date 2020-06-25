def solution(l,t):
  for i in range(0,len(l)):
    sum_=l[i]
    for j in range(i+1,len(l)):
      if(sum_==t):
        return [i,j-1]
      if(j==len(l) or (sum_>t)):
        break
      sum_+=l[j]
  return [-1,-1]
      
