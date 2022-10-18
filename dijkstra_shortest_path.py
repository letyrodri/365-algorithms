from queue import PriorityQueue

def dijkstra_shortest_path(graph, s):
	"""
	graph is adyacency list where each list has a tuple (v, w) target node and weight
	"""

	pq = PriorityQueue()
	S = set()

	pq.put( (0,s) )

	parents = [None for x in range(len(graph))]
	cost = [float("inf") for x in range(len(graph))]
	cost[s] = 0
	
	while (not pq.empty()):
		u = pq.get()[1]
		if u not in S:
			S.add(u)

			for (v,w) in graph[u]:
				pq.put( (w,v) )


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



	
