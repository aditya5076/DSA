""" using queue we gonna make BFS"""

class Node(object):
    def __init__(self,name):
        self.name=name
        self.adjancy_list=[]
        self.visited=False
        self.predecessor=None

class BFS(object):
    def bfs(self,startNode):
        queue=[]
        queue.append(startNode)
        startNode.visited=True

        while queue:

            actualNode=queue.pop(0)
            print(actualNode.name)

            for n in actualNode.adjancy_list:
                if not n.visited:
                    n.visited=True
                    queue.append(n)

node1=Node('A')
node2=Node('B')
node3=Node('C')
node4=Node('D')
node5=Node('E')

node1.adjancy_list.append(node2)
node1.adjancy_list.append(node3)
node2.adjancy_list.append(node4)
node2.adjancy_list.append(node5)
"""     A
    B       C
D       E
"""
bfs=BFS()
bfs.bfs(node1)


