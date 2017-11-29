from abc import ABC, abstractmethod


class Graph(ABC):

    def __init__(self, nodes = [], edges = []):
        """
            Initializer for Graph abstract class.

        Args:
            None

        Returns:
            None

        Raises:
            Nothing
        """

        self._nodes = nodes
        self._edges = edges

    @abstractmethod
    def get_nodes(self):
        return self._nodes

    @abstractmethod
    def get_edges(self):
        return self._edges

class DirGraph(Graph):

    def __init__(self, nodes = [], edges = []):
        super().__init__(nodes, edges)


    def get_nodes(self):
        super().get_nodes()

    def get_edges(self):
        super().get_edges()





