import json
import random
import sys
from typing import List
import matplotlib.pyplot as plt

from src.Node import Node
from src.DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self._graph = graph
        self.get_graph().set_mc(0)

    # loading a graph from a json file
    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, encoding='utf-8') as f:
                json_string = f.read()
            a = json.loads(json_string)  # reading the file
            new_g = DiGraph()
            if a.get('Nodes')[0].get('pos') is not None:  # if the nodes have a position in the file
                for node in a.get('Nodes'):
                    pos = tuple([float(a) for a in node.get('pos').split(",")])  # save the pos a tuple
                    new_g.add_node(node.get('id'), pos)  # add the node to the graph
            else:
                for node in a.get('Nodes'):  # if the nodes don't have a position in the file
                    new_g.add_node(node.get('id'))  # add the node without a position
            for edge in a.get('Edges'):
                new_g.add_edge(edge.get('src'), edge.get('dest'), edge.get('w'))  # add all edges to the graph
            self._graph = new_g  # initiating the graph
            return True
        except Exception as e:
            print(e)
            return False

    # saving the graph onto a json file
    def save_to_json(self, file_name: str) -> bool:
        try:
            json_nodes, json_edges = [], []  # creating lists for nodes and edges
            for node in self._graph._nodes.values():  # adding all the nodes to the node list
                x_val, y_val, z_val = node.getPos()
                node_dict = {'pos': '{x},{y},{z}'.format(x=x_val, y=y_val, z=z_val), 'id': node.getID()}
                json_nodes.append(node_dict)
            for source, dicts in self._graph._inedges.items():  # adding all the edges to the graph list
                for weight, dst in dicts.items():
                    edge_dict = {'src': source, 'w': weight, 'dest': dst}
                    json_edges.append(edge_dict)
            json_dict = {'Edges': json_edges, 'Nodes': json_nodes}
            json_string = json.dumps(json_dict)  # creating the json file from the lists
            with open(file_name, "w") as f:
                f.write(json_string)
            return True
        except Exception as e:
            print(e)
            return False

    # finding the shortest path between 2 nodes, returning the path as well as it's weight
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        prev, dist = self.DijkstraAlgo(id1)  # running the dijkstra algorithm
        path = []
        nd = prev[id2]
        while (nd != None and prev[nd.getID()] != None):
            path.insert(0, nd.getID())  # adding the nodes to the path
            nd = prev[nd.getID()]

        if nd != None:
            path.insert(0, nd.getID())

        path.append(id2)  # adding the destination node to the path

        return ((dist[id2], path))

    def DijkstraAlgo(self, src):
        visit = []
        dist = []
        prev = []
        for i in range(self._graph.v_size()):
            visit.append(i)  # adding the nodes to the list of visited nodes
            dist.append(sys.maxsize)  # setting the distance to all to "infinity"
            prev.append(None)  # the previous node to all is null at the start of the algorithm
        dist[src] = 0  # distance from source to itself is 0

        while (visit):
            lowerIndex = 0
            lowerValue = dist[visit[lowerIndex]]
            for i in range(len(visit)):
                if (lowerValue > dist[visit[i]]):  # finding the index with the lowest value
                    lowerIndex = i
                    lowerValue = dist[visit[i]]
            edges = self._graph.all_out_edges_of_node(visit[lowerIndex])
            for dst, weight in edges.items():  # checking all adjacent nodes
                alt = dist[visit[lowerIndex]] + weight
                if (alt < dist[dst]):
                    dist[dst] = alt
                    prev[dst] = self._graph.getNode(visit[lowerIndex])

            visit.remove(visit[lowerIndex])

        return prev, dist

    def plot_graph(self) -> None:
        for src in self._graph.get_all_v().values():
            x, y = random.uniform(35.15000000000, 35.25000000000), random.uniform(32.00000000000, 32.10500000000)  # if node doesn't have a position create a random position
            if src.getPos():
                x, y = src.getPos()[0], src.getPos()[1]
            else:
                src.setPos((x, y))

            plt.plot(x, y, markersize=10, marker="o", color="blue")
            plt.text(x, y, str(src.getID()), color="red", fontsize=12)
            for dst in self._graph.all_out_edges_of_node(src.getID()).keys():

                x2, y2 = random.uniform(35.15000000000, 35.25000000000), random.uniform(32.00000000000, 32.10500000000)
                if self._graph.getNode(dst).getPos(): # if node doesn't have a position create a random position
                    x2, y2 = src.getPos()[0], src.getPos()[1]
                else:
                    self._graph.getNode(dst).setPos((x2, y2))

                x2, y2 = self._graph.getNode(dst).getPos()[0], self._graph.getNode(dst).getPos()[1]
                plt.annotate("", xy=(x, y), xytext=(x2, y2), arrowprops=dict(arrowstyle="<-"))
        plt.show()

    # returning the graph
    def get_graph(self) -> GraphInterface:
        return self._graph

    # Computes a list of consecutive nodes which go over all the nodes in cities.
    # Same as the "Traveling Salesman Problem"
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if not node_lst:  # if cities list is empty return null
            return None
        if not self.isConnected():  # if the graph isn't connected return null
            return None
        totalWeight = 0
        salesman = []
        start = node_lst[0]
        salesman.append(start)  # adding to the list the starting city
        for node in node_lst:  # loop on all the cities and find for them the shortest path
            dst = node
            if dst in salesman:
                continue

            weight, path = self.shortest_path(start, dst)
            for j in path:  # loop on all nodes that are part of the path from one city to another
                if not j == start:
                    salesman.append(j)  # add them to the list
                    totalWeight += weight

            start = dst  # update the starting city for the next iteration

        return salesman, totalWeight

    def centerPoint(self) -> (int, float):
        if not self.isConnected():  # if the graph isn't connected then we return null (there is no center)
            return None
        maxDis = sys.maxsize  # max value so we can find the shortest path
        nodeKey = 0
        nodes = self._graph.get_all_v()
        for node in nodes.values():  # finding the max shortest path to all others nodes
            src = node.getID()
            maxShortPath = 0
            nodes2 = self._graph.get_all_v()
            for dst in nodes2.values():  # finding the shortest path for each node
                if (dst != node):
                    checkPath = self.shortest_path(src, dst.getID())
                    dist = checkPath[0]
                    if (dist > maxShortPath):
                        maxShortPath = dist
            if (maxShortPath < maxDis):
                maxDis = maxShortPath
                nodeKey = src  # setting the center node of the graph

        return (nodeKey, maxDis)

    # //Iterative DFS, in recursive DFS we had problem with stack overflow in bigger graphs
    def DFS(self, node: Node):
        node.setTag(1)  # set the tag to be 1, same as saying we visited the node
        stack = []
        stack.append(node)
        while not stack:
            node = stack[0]
            stack.pop()
            for edge in self._graph.all_out_edges_of_node(node.getID()):  # checking all adjacent edges
                dest = self._graph.getNode(edge)
                if dest.getTag() == 0:  # if we haven't visited them yet, add them to the stack
                    stack.append(dest)

    def runDFS(self, graph: DiGraph) -> bool:
        for node in graph._nodes.values():
            node.setTag(0)  # setting the tag of all nodes to be 0
        for node in graph._nodes.values():  # visiting all nodes in the graph
            if node.getTag() == 0:
                self.DFS(node)  # if we haven't visited them yet run DFS
        for node in graph._nodes.values():
            if node.getTag == 0:  # if one of the nodes has a tag==0 the graph is not connected
                return False
        return True

    # Function to check if the graph is strongly connected. Checked by running DFS algorithm on the graph,
    # reversing the edges of the graph and running the DFS algorithm again
    def isConnected(self) -> bool:
        if self._graph.e_size() < self._graph.v_size():  # there are less than n edges
            return False
        reverse = DiGraph()
        for node in self._graph._nodes.values():  # reversing the graph
            reverse.add_node(node.getID(), node.getPos())  # adding the nodes
        for source, dicts in self._graph._inedges.items():  # adding the edges but in a reversed way
            for weight, dst in dicts.items():
                reverse.add_edge(source, dst, weight)  # src = dest, dest = src
        return self.runDFS(self._graph) and self.runDFS(reverse)
