import networkx as nx
from arler.Thinking.Agent import Variable
from arler.Utilities.build import buildTrajectoryScaffold


class Trajectory:
    def __init__(self, blueprint):
        self.__scaffold__ = buildTrajectoryScaffold(blueprint, Variable)

    @property
    def size(self):
        return len(self.__scaffold__) - 2

    def getSharedContextBetween(self, parent, child):
        return self.__scaffold__[parent][child]["variables"]

    def haveIdenticalRelevance(self, *args):
        pass
