from unittest import TestCase

from src.GraphAlgo import GraphAlgo


class TestDiGraph(TestCase):

    def test_get_mc(self):
        g_algo = GraphAlgo()
        for n in range(3):
            g_algo.get_graph().add_node(n)
        g_algo.get_graph().add_edge(0, 1, 2)
        g_algo.get_graph().add_edge(1, 2, 2.5)
        g_algo.get_graph().add_edge(2, 1, 5.2)
        g_algo.get_graph().remove_node(0)
        self.assertEqual(7, g_algo.get_graph().get_mc())

    def test_get_node(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        node=g_algo.get_graph().getNode(1).getID()
        self.assertEqual(node,1)

    def test_v_size(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        self.assertEqual(17,g_algo.get_graph().v_size())

    def test_e_size(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        self.assertEqual(36, g_algo.get_graph().e_size())

    def test_add_edge(self):
        g_algo = GraphAlgo()
        g_algo.get_graph().add_node(8, (28.12364, 22.426164, 0))
        g_algo.get_graph().add_node(3, (28.32364, 25.346164, 0))
        g_algo.get_graph().add_edge(3, 8, 2.5)
        self.assertEqual({3: 2.5}, g_algo.get_graph().all_in_edges_of_node(8))

    def test_add_node(self):
        g_algo = GraphAlgo()
        g_algo.get_graph().add_node(8, (28.12364, 22.426164, 0))
        g_algo.get_graph().add_node(3, (28.32364, 25.346164, 0))
        g_algo.get_graph().add_edge(3, 8, 2.5)
        self.assertEqual(3, g_algo.get_graph().getNode(3).getID())

    def test_remove_node(self):
        g_algo = GraphAlgo()
        for n in range(3):
            g_algo.get_graph().add_node(n)
        g_algo.get_graph().add_edge(0, 1, 2)
        g_algo.get_graph().add_edge(1, 2, 2.5)
        g_algo.get_graph().add_edge(2, 1, 5.2)
        # g_algo.get_graph().remove_node(0)
        self.assertEqual(True, g_algo.get_graph().remove_node(0))

    def test_remove_edge(self):
        g_algo = GraphAlgo()
        for n in range(3):
            g_algo.get_graph().add_node(n)
        g_algo.get_graph().add_edge(0, 1, 2)
        g_algo.get_graph().add_edge(1, 2, 2.5)
        g_algo.get_graph().add_edge(2, 1, 5.2)
        # g_algo.get_graph().remove_node(0)
        self.assertEqual(True, g_algo.get_graph().remove_edge(0,1))

    def test_get_all_v(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        self.assertEqual(17, g_algo.get_graph().v_size())

    def test_all_in_edges_of_node(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        self.assertEqual({0: 1.232037506070033, 2: 1.5784991011275615},g_algo.get_graph().all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        self.assertEqual({0: 1.8635670623870366, 2: 1.8015954015822042}, g_algo.get_graph().all_out_edges_of_node(1))

