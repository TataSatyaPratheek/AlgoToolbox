# python3
import sys
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
      return -1
    if current_refil <= n:
      num_refil +=1
  return num_refil

def compute_min_refills(distance, tank, stops):
    # write your code here
		stops = [0] + stops + [distance]
		
		return greedy_no_refils(stops, len(stops)-2, tank)
		
if __name__ == '__main__':
	d, m, _, *stops = map(int, sys.stdin.read().split())
	print(compute_min_refills(d, m, stops))
