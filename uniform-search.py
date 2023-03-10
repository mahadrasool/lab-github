import math

class UCS():
    def __init__(self):
        self.initialState = 'C'
        self.goalState = 'B'

    def UCS(self):
        self.graph = {
            'A':Node('A',None,[('B',6),('C',9),('E',1)], 0),
            'B':Node('B',None,[('A',6),('D',3),('E',4)], 0),
            'C':Node('C',None,[('A',9),('F',2),('G',3)], 0),
            'D':Node('D',None,[('B',3),('E',5),('F',7)], 0),
            'E':Node('E',None,[('A',1),('B',4),('D',5),('F',6)], 0),
            'F':Node('F',None,[('C',2),('E',6),('D',7)], 0),
            'G':Node('G',None,[('C',3)], 0)
        }
        frontier = dict()
        frontier[self.initialState] = (None,0)
        explored = []

        while len(frontier) != 0:
            currentNode = self.findMin(frontier)
            del frontier[currentNode]
            if self.graph[currentNode].state == self.goalState:
                return self.actionSequence(self.graph,self.initialState, self.goalState)
            
            explored.append(currentNode)

            for child in self.graph[currentNode].action:
                currentCost = child[1] + self.graph[currentNode].totalcost

                if child[0] not in frontier and child[0] not in explored:
                    self.graph[child[0]].parent = currentNode
                    self.graph[child[0]].totalcost = currentCost
                    frontier[child[0]] = (self.graph[child[0]].parent, self.graph[child[0]].totalcost)
                elif child[0] in frontier:
                    if frontier[child[0]][1] < currentCost:
                        self.graph[child[0]].parent = frontier[child[0]][0]
                        self.graph[child[0]].totalcost= frontier[child[0]][1]

                    else:
                        frontier[child[0]] = (currentNode,currentCost)
                        self.graph[child[0]].parent = frontier[child[0]][0]
                        self.graph[child[0]].totalcost = frontier[child[0]][1]        

    def findMin(self,frontier):
        minV = math.inf
        node = ''
        for i in frontier:
            if minV > frontier[i][1]:
                minV = frontier[i][1]
                node = i
        return node

    def actionSequence(self,graph, initialState, goalState):
        solution = [goalState]
        currentParent = graph[goalState].parent

        while currentParent is not None:
            solution.append(currentParent)
            currentParent = graph[currentParent].parent
        solution.reverse()
        return solution



class Node:
    def __init__(self,state,parent,action,totalcost):
        self.state = state
        self.parent = parent
        self.action = action
        self.totalcost = totalcost




search = UCS()
solution = search.UCS()
print(solution)