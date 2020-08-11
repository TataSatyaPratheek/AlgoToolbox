#First greedy algorithm implementation
import numpy as np
def greedy_no_refils(x,n, L):
  #x is the distance array of stops along the way from the initial spot
  #n is the number of gas stops 
  #L is the longest distance the car can travel on a full tank
  current_refil = 0
  num_refil = 0
  while current_refil <=n:
    last_refil = current_refil
    while (current_refil<=n and x[current_refil+1]-x[last_refil] <= L):
      current_refil +=1
    if current_refil == last_refil:
      return 'IMPOSSIBLE!'
    if current_refil <= n:
      num_refil +=1
  return num_refil

a = np.array([0,3,4,7,9,11,14,15,18,22])
b =len(a)-2
c = 4
print(greedy_no_refils(a,b,c))