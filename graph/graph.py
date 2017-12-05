from abc import ABC, abstractmethod

class Node:

    def __init__(self, value, PRScore = 0, ID, neighbors):
        """
            Initializer for Node element.

        Args:
            value = STR value assigned to the Noded (it could be a single keyword or a whole sentence)
            PRScore= INT value with the score assigned by TextRank algorithm
            ID = INT eventual sentence ID needed for sentence postprocessing

        Returns:
            A node instance with value and PageRank score assigned to it

        Raises:
            Nothing
        """

        self._value = value
        self._PRscore = PRScore
        self._ID = ID

    @property
    def get_value(self):
        return self._value

    @property
    def get_PRScore(self):
        return self._PRscore

    @property
    def get_ID(self):
        return self._ID


class Arc:

    def __init__(self, weight, node1, node2):
       """ TODO """

       self._weight = weight
       self._node1 = node1
       self._node2 = node2


    @property
    def get_weight(self):
        return self._weight

    @property
    def get_node1(self):
        return self._node1

    @property
    def get_node2(self):
        return self._node2



class Graph(ABC):


    num_nodes = 0

    def __init__(self, nodes = {} ):
        """
        Initializer for Graph abstract class.

        Args:
            nodes = DICT dictionary implementing the graph.
                    key: Node -> Value: LIST list of neighbors
        Returns:
            None

        Raises:
            Nothing
        """
        if len(nodes):
            self.num_nodes = len(nodes)

        self._nodes = nodes

    @abstractmethod
    def get_nodes(self):
        return self._nodes

    @classmethod
    def graph_size(cls):
        return cls.num_nodes

    def add_node(self, node):
        pass


class UndirGraph(Graph):

    def __init__(self, nodes = [], edges = []):
        super().__init__(nodes, edges)

    def get_nodes(self):
        super().get_nodes()

    def build_graph(self, elem_list):
        """
        Builds a graph taking a list of processed words or sentence as input

        Args:
            elem_list: STR_LIST list = processed words or sentend needed to build the graph
        Returns:
            A dictionary implementing the graph

        Raises:
            Nothing
        """
        pass




