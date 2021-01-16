""" using recursion we gonna make DFS, also can be done using stack ADT """
class Node(object):
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.adjancy_list=[]
        self.predecessor=None

class DFS(object):
    # def dfs(self,node):

    #     node.visited=True
    #     print(node.name)
    #     for n in node.adjancy_list:
    #         if not n.visited:
    #             self.dfs(n)

    def dfs(self,startNode):
        queue=[]
        queue.append(startNode)
        n=len(queue)
        startNode.visited=True

        while queue:

            actualNode=queue.remove(n)
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
node4.adjancy_list.append(node5)
""" pictorial view
            A
        B       C
    D
E
"""

dfs=DFS()
dfs.dfs(node1)