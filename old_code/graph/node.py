class Node:

    def __init__(self, value, ID = 0, PRScore = 0, prevPR = 0):
        """
            Initializer for Node element.

        Args:
            value = STR value assigned to the Noded (it could be a single keyword
                    or a whole sentence)
            ID = INT eventual sentence ID needed for sentence postprocessing
            PRScore= INT value with the score assigned by TextRank algorithm
            prevPR = INT value storing previous iteration value of TextRank

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

    @classmethod
    def link_nodes(n1, n2, weight = 1):
        """ Returns an Arc object linking two nodes passed as argument. """
        arc = Arc(n1, n2, weight)

    def __str__(self):
        seq = ['Value: ', self._value,
                '| Current PRScore: ', str(self._PRScore),
                '| ID: ', str(self._ID),
                '| Difference PRScore: ', str(self.diff_PR), "\n"
            ]
        return "\t".join(seq)


class Arc:

    def __init__(self, node1, node2, weight = 1):

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


