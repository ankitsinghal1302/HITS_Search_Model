import cjson
import networkx as nx
G = nx.DiGraph()
graph = {}
largest_weakly_cc = nx.DiGraph()



def get_adjacency_list():
    	i=0
	data = {}
	with open('/home/ankit/Desktop/tweets.txt','r') as f:
		for line in f:
			data.update({i:cjson.decode(line)})
			i = i+1
	
	for k,v in data.iteritems():
		user = v['user']
		value = []
		key = user['screen_name']
		entities = v['entities']
		user_mentions = entities['user_mentions']
		for item in user_mentions:
			value.append(item['screen_name'])
		
		if graph.has_key(key):
			
			value.extend(list(graph[key]))
			
			value = set(value)
			graph.update({key:value})
		else :
			value = set(value)
			graph.update({key:value})

def form_graph():
	for k,v in graph.iteritems():
		G.add_node(k)
	

	for k,v in graph.iteritems():
		for item in v:
			if G.has_edge(k,item) == False and item != k:
				G.add_edge(k,item)

get_adjacency_list()
form_graph()
k = 0
for w in nx.weakly_connected_component_subgraphs(G):
    if k< nx.number_of_nodes(w):
	k = nx.number_of_nodes(w)
	largest_weakly_cc = w



