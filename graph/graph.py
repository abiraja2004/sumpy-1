from abc import ABC, abstractmethod

from node import *


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

        """
        TODO better handle when both unproc_nodes and dict_graph are passed
               as arguments
        """
        if unproc_nodes and dict_graph:
            print("ERROR, cannot have both a list of nodes and a graph of nodes as"
                    + "arguments for the Graph Constructor"
                    )
            exit(1)

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

        # it replace
        #for i, elem in enumerate(node_list):
        #    temp_node = Node(elem, i)
        #    node_list[i] = temp_node

        for vertex in node_list:
            self._num_nodes = self._num_nodes + 1
            #vertex.ID = self._num_nodes
            graph[vertex] = []
        """ TODO build graph according to similarity method """

        print('num nodes', self._num_nodes)
        print(graph)
        assert len(graph) == self._num_nodes
        return graph

    def add_node(self, node, arc =[]):
        """
            Add new node to the Graph. It updates the node if it exsist.

        It add the node and the arc to the graph. If the node is already in the
        graph it is updated with adding the list of arcs as its neighbors

        Args:
            node: NODE elem to be added to the graph
            arc: LIST[ARC] element containing the neighbors of the node
        Returns:
            Nothing
        Raises:
            Nothing
        """


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
