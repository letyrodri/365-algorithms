from queue import PriorityQueue

def dijkstra_shortest_path(graph, s):
	"""
	graph is adyacency list where each list has a tuple (v, w) target node and weight
	"""

	pq = PriorityQueue()
	s = set()

	pq.put( (0,s) )

	parents = [None for x in range(len(graph))]
	cost = [0 for x in range(len(graph))]

	
	while (not pq.empty()):
		u = pq.get()
		s.append(u)
		
		for (v,w) in graph[u]:
			pq.put( (w,v) )

			if cost[v] is None or cost[v] > cost[u]+w:
				cost[v] = cost[u]+w
				parents[v] = u

	return parents				



	
