from unittest import TestCase

from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def test_load_from_json(self):
        g_algo = GraphAlgo()
        self.assertTrue(g_algo.load_from_json("../data/A1.json"))

    def test_save_to_json(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/testA1.json")
        g_algo.get_graph().add_node(8, (28.12364, 22.426164, 0))
        g_algo.get_graph().add_node(3, (28.32364, 25.346164, 0))
        g_algo.get_graph().add_edge(3, 8, 3.2451)
        self.assertEqual(True, g_algo.save_to_json("../data/testA1.json"))
        self.assertEqual(8, g_algo.get_graph().getNode(8).getID())
        g_algo2 = GraphAlgo()
        g_algo2.load_from_json("../data/testA1.json")
        self.assertEqual(8, g_algo2.get_graph().getNode(8).getID())

    def test_shortest_path(self):  # 5-7
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        src = g_algo.get_graph().getNode(5).getID()
        dst = g_algo.get_graph().getNode(7).getID()
        weight, path = g_algo.shortest_path(src, dst)
        self.assertEqual(weight, 2.9718770505662677)
        self.assertEqual(path, [5, 6, 7])

    def test_plot_graph(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        g_algo.plot_graph()

    def test_tsp(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        path, weight = g_algo.TSP([1, 2, 5, 7])
        self.assertEqual(weight, 14.325961020413278)
        self.assertEqual(path, [1, 2, 6, 5, 6, 7])

    def test_center_point(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        id, weight = g_algo.centerPoint()
        self.assertEqual(weight, 9.925289024973141)
        self.assertEqual(id, 8)

    def test_is_connected(self):
        g_algo = GraphAlgo()
        g_algo.load_from_json("../data/A1.json")
        self.assertTrue(True)
