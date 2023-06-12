import math
import random
import networkx as nx
from pyvis.network import Network


def generate_ospf(routers, source_router, target_router):
    random.seed(1)
    edge = nx.complete_graph(routers)
    for (u, v) in edge.edges():
        edge.edges[u, v]['weight'] = random.randint(1, 100)
    return edge, source_router, target_router


def draw_ospf(edge, source_router, target_router):
    # Calculate the shortest path between the source and target routers
    shortest_path = nx.shortest_path(edge, source=source_router, target=target_router, weight='weight')
    shortest_path_edges = set(zip(shortest_path, shortest_path[1:]))

    # Create a Pyvis network with 100% width and height of the browser window
    net = Network(notebook=True, height="100vh", width="100%")
    # Add nodes and edges to the network
    angle = 2 * math.pi / len(edge.nodes())
    for i, node in enumerate(edge.nodes()):
        # Calculate the position of the node
        x = 500 * math.cos(i * angle)  # 500 is the radius of the circle
        y = 500 * math.sin(i * angle)
        net.add_node(node, x=x,y=y,label=str(node), title=str(node), smooth=False, physics=False, set_node_positon=False, font={'size': 30, 'align':'right', 'color':'#880808'},
                     color='green' if node == source_router or node == target_router else 'lightblue' )
    for u, v, data in edge.edges(data=True):
        color = 'red' if (u, v) in shortest_path_edges or (v, u) in shortest_path_edges else 'grey'
        net.add_edge(u, v, title=str(data['weight']), font={'size': 40, 'align':'top'}, width=6, color=color, smooth=False,
                     physics=False,
                     label=str(data['weight'], ))

    # Set the layout for the network
    net.barnes_hut(gravity=-8000, central_gravity=0.3, spring_length=100, spring_strength=0.001, damping=0.09)

    # Save the network to an HTML file
    net.show("static/PyNet.html")
