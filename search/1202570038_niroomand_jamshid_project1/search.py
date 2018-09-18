# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


# implementing tree search algorithm from the psedocode in the book on page 82 in the book


def genericSearch(problem, fringe):

    explored = []
    initialState = problem.getStartState()
    fringe.push((initialState, []))

    while not fringe.isEmpty():
        node, state = fringe.pop()
        if problem.isGoalState(node):
            return state
        if node not in explored:
            explored.append(node)

            for successor, action, pathCost in problem.getSuccessors(node):
                if successor not in explored:
                    nextState = state + [action]
                    childNode = (successor, nextState)
                    fringe.push(childNode)
    return None

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    # setting frontier to empty stack
    fringe = util.Stack()
    # calling the helper funciton generic search on the stack 
    return genericSearch(problem, fringe)

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # setting fringe to Queue 
    fringe = util.Queue()
    # calling the helper function genericSearch to accomplish the breadFirstSearch
    return genericSearch(problem, fringe)
   


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"


    # defining a function to consider cost of each path 
    def UCS((node, cost)):
        return problem.getCostOfActions(cost)

    # calling PriorityQueueWithFunction from util which is avaible for us and setting it to the fringe
    fringe = util.PriorityQueueWithFunction(UCS)

    # here returning the uniform cost search with the help of generic search
    return genericSearch(problem, fringe)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0




def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # defining aStar function to take under consideration the path cost and heuristic
    # accomplishing this with the help of getCostActions which is avaible to us 
    def aStar((node, state)):
        return problem.getCostOfActions(state) + heuristic(node, problem)
    # calling PriorityQueueWithFunction from util and setting it to fringe 
    fringe = util.PriorityQueueWithFunction(aStar)
    # calling the generic search to accomplish aStateSearch 
    return genericSearch(problem, fringe)


    util.raiseNotDefined()

 
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


