from abc import ABC, abstractmethod

class Node:

    def __init__(self, value, ID = 0, PRScore = 0, prevPR = 0):
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
        self._PRScore = PRScore
        self._ID = ID
        self._prevPR = prevPR


    @property
    def value(self):
        return self._value

    @property
    def PRScore(self):
        return self._PRScore

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def prevPR(self):
        return self._prevPR

    @property
    def diff_PR(self):
        """
            Returns the diff between current and previous PageRank score.

        Args:
            None

        Returns:
            An integer showing the difference between current and previous PRScore.
            When diffPR is below a given treshold for any Node in the graph PageRank
            algorithm shall stop

        Raises:
            Nothing
        """
        return self._PRScore - self._prevPR

    def __str__(self):
        seq = ['Value: ', self._value,
                '| Current PRScore: ', str(self._PRScore),
                '| ID: ', str(self._ID),
                '| Difference PRScore: ', str(self.diff_PR), "\n"
            ]
        return "\t".join(seq)


class Arc:

    def __init__(self, node1, node2, weight = 1):
       """ TODO """

       self._weight = weight
       self._node1 = node1
       self._node2 = node2


    @property
    def weight(self):
        return self._weight

    @property
    def node1(self):
        return self._node1

    @property
    def node2(self):
        return self._node2



class Graph(ABC):

    def __init__(self, unproc_nodes = [], dict_graph = {}):
        """
        Initializer for Graph abstract class.

        Args:
            unproc_nodes = STR_LIST containing processed lemmatized/tokenized/tagged                           text
            dict_graph = DICT dict implementing the graph
                        KEY: nodes -> VALUE: list of arc (neighbors)
        Returns:
            An initialized graph

        Raises:
            Nothing
        """

        """ TODO handle case when both list and graph are passed as arguments """

        if dict_graph:
            self._graph = dict_graph
            self._num_nodes = len(self._graph)
        else:
            self._graph = self.build_graph(unproc_nodes)

    @property
    def graph(self):
        return self._graph

    @property
    def size(self):
        return self._num_nodes

    @abstractmethod
    def build_graph(self, nodes_list = []):
        pass

    @abstractmethod
    def add_node(self, node, arc):
        pass

    @abstractmethod
    def del_node(self, node):
        pass

class UndirGraph(Graph):

    def __init__(self, unproc_nodes = [], graph_dict = {}):
        super().__init__(unproc_nodes)

    def build_graph(self, node_list):
        """
        Builds a graph taking a list of processed words or sentence as input

        Args:
            node_list: STR_LIST = processed words or sentend needed to build the graph
        Returns:
            A dictionary implementing the graph

        Raises:
            Nothing
        """
        graph = {}

        self._num_nodes = 0

        for vertex in node_list:
            self._num_nodes = self._num_nodes + 1
            vertex.ID = self._num_nodes
            graph[vertex] = []
        """ TODO build graph according to similarity method """

        assert len(graph) == self._num_nodes
        return graph

    def add_node(self, node, arc):
        pass

    def del_node(self, node):
        pass

    def __str__(self):
        final = []
        for vertex in self._graph:
            seq = ['Value: ', vertex.value,
                        '| Current PRScore: ', str(vertex.PRScore),
                        '| ID: ', str(vertex.ID),
                        '| Difference PRScore: ', str(vertex.diff_PR), "\n"]
            elem = "\t".join(seq)
            final.append(elem)
        return ''.join(final)
