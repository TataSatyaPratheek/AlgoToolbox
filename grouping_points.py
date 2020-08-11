"""
you have a finite set of points given to you, you have to find a way to group 
them in such a way that for any two members of a group, their distance is not 
more than a unit, with the least number of groups.
"""

def greedy_grouping(given_points):
  
	#part one of the solution, sorting the elements monotonically
  
	sort_points = sorted(given_points)
  
	#part two is to actually implement the greedy algo to partition the folks 
  #satisfying the given condition
	
	R =set()
	i = 0
	while i<len(given_points):
		[l, r] = [sort_points[i], sort_points[i]+1]
		R = R.union(set([l,r]))
		i +=1
		while i<len(given_points) and sort_points[i]<=r:
			i+=1
	return sorted(list(R))

a = [1.1,1.2,1.3,1.5,1.8,1.9,2.5,2.9,3.4,3.8,3.9,5.8,7.9]
print(greedy_grouping(a))
#break the list pair wise to get the partitions