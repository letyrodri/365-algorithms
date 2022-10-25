class PriorityQueue:
	

	def __init__(self):
		self.elements = list()
		

	def size(self):
		return len(self.elements)

	def push(self, priority, value):
		if self.size() == 0:
			self.elements.append( (priority, value) )

		else:
			p = 0 

			while (p < self.size() and self.elements[p][0] < priority):
				p+=1

			if p == self.size():
				self.elements.append( (priority, value))
			else:
				self.elements.insert(p, (priority, value))

	def change_priority(self, value, new_priority):
		p = 0 

		while (p < self.size() and self.elements[p][1] != value):
			p+=1	

		if p < self.size():
			del self.elements[p]
			self.push(new_priority, value)

	def pop(self):
		v = self.elements[0][1]
		del self.elements[0]
		return v

	def empty(self):
		return len(self.elements) == 0

def dijkstra_shortest_path(graph, s):
	"""
	graph is adyacency list where each list has a tuple (v, w) target node and weight
	"""

	n = len(graph)
	S = set()
	pq = PriorityQueue()
	

	pq.push(0,s)
	for x in range(1,n):
		pq.push(float("inf"),x)

	parents = [None for x in range(len(graph))]
	cost = [ float("inf") for x in range(len(graph))]
	cost[s] = 0
	
	while (not pq.empty()):
		u = pq.pop()
		if u not in S:
			S.add(u)

			for (v,w) in graph[u]:
				pq.change_priority( v, w )


				if v!=s:
					if cost[v] == float("inf"):
						cost[v] = cost[u]+w
						parents[v] = u
					else:
						if cost[v] > cost[u]+w:
							cost[v] = cost[u]+w
							parents[v] = u

	return parents, cost


g = [[(1,2),(2,4),(4,1)],[(0,2),(2,1)],[(0,4),(1,2),(3,1)],[(2,1),(4,1)],[(0,1),(3,1)]]	

print(dijkstra_shortest_path(g,0))			



	
