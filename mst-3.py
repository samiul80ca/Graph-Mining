graph_dict = {  "0":{"1":0, "2":0, "3":0 },
                "1":{"0":0, "2":0},
                "2":{"0":0, "1":0, "3":0, "4":0},
                "3":{"0":0, "2":0, "5":0},
                "4":{"2":0, "5":0, "6":0, "7":0, "8":0},
                "5":{"3":0, "4":0, "6":0, "7":0, "8":0},
                "6":{"4":0, "5":0, "7":0, "8":0},
                "7":{"4":0, "5":0, "6":0, "8":0},
                "8":{"4":0, "5":0, "6":0, "7":0}
                }

g = {}
edges = {}
mst = []
#n = int(input(('Enter the number of nodes: ')))
n = 5
for i in graph_dict:
    g[i] = 1
src = input('Enter the source node: ')
edges[src] = 'None'
g[src] = 0
print(g)
while g:
    print('Map:  ',g)
    extract_min = list(min(zip(g.values(), g.keys())))
    print(extract_min)
    minimum_value  = extract_min[0]
    minimum_node = extract_min[1]
    print('Minimum-->',minimum_node)
    if edges[minimum_node]!='None':
        mst.append(edges[minimum_node])
    neighbours = [i for i in graph_dict[minimum_node].keys()]
    print('neighbours ',neighbours )
    for nei in neighbours:
        print('nei: ',nei)
        if nei in g.keys():
            if graph_dict[minimum_node][nei] <= g[nei]:
                g[nei] = graph_dict[minimum_node][nei]
                edges[nei] = (minimum_node, nei)
    g.pop(minimum_node)


print('Minimum spanning tree: ',mst)