from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self._nodes = {}
        self._inedges = {}
        self._outedges = {}
        self._mc = 0

        self.__edgesCounter_ = 0
        self.__nodesCounter_ = 0

    # returning a requested node by it's id
    def getNode(self, node_id) -> Node:
        return self._nodes[node_id]

    # returning the amount of nodes in the graph
    def v_size(self) -> int:
        return self.__nodesCounter_

    # returning the amount of edges in the graph
    def e_size(self) -> int:
        return self.__edgesCounter_

    # returning the mc of the graph
    def get_mc(self) -> int:
        return self._mc

    # setting mc
    def set_mc(self, mc):
        self._mc = mc

    # connecting 2 nodes with an edge with a given weight
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self._outedges.keys() or id2 not in self._inedges.keys():
            return False

        if id2 in self._outedges[id1].keys() or id1 in self._inedges[id2].keys():
            return False
        self._outedges[id1][id2] = weight
        self._inedges[id2][id1] = weight

        self.__edgesCounter_ += 1
        self._mc += 1
        return True

    # adding a new node to the graph
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self._nodes.keys():
            return False

        nd = Node(node_id, pos)
        self._nodes[node_id] = nd

        self._inedges[node_id] = {}  # adding to in edges dictionary
        self._outedges[node_id] = {}  # adding to out edges dictionary

        self.__nodesCounter_ += 1
        self._mc += 1
        return True

    # removing a node from the graph
    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes:  # if the id of the node not in the graph
            return False

        self._nodes.__delitem__(node_id)
        for edge in self._outedges[node_id]:  # deleting all the out edges using that node
            self._inedges[edge].__delitem__(node_id)
            self.__edgesCounter_ -= 1

        for edge in self._inedges[node_id]:  # deleting all the in edges using that node
            self._outedges[edge].__delitem__(node_id)
            self.__edgesCounter_ -= 1

        self._outedges.__delitem__(node_id)  # deleting the id from the out edges dictionary
        self._inedges.__delitem__(node_id)  # deleting the id from the in edges dictionary
        self._mc += 1
        return True

    # removing an edge from the graph
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self._outedges.keys() or node_id2 not in self._inedges.keys():  # checking if both ids are in the graph
            return False

        if node_id2 not in self._outedges[node_id1] or node_id1 not in self._inedges[node_id2]:
            return False

        self._outedges[node_id1].__delitem__(node_id2)  # deleting the edge
        self._inedges[node_id2].__delitem__(node_id1)
        self.__edgesCounter_ -= 1
        self._mc += 1
        return True

    # returning all the nodes of the graph
    def get_all_v(self) -> dict:
        return self._nodes

    # returning all in edges of the graph
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self._inedges[id1]

    # returning all out edges of the graph
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._outedges[id1]

    def __repr__(self):
        return f"DiGraph:\n" \
               f"Node({self._nodes})\n" \
               f"Edges({self._outedges})"
