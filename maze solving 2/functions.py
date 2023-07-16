class Node:
    def __init__(self, state,action , parent):
        self.state = state
        self.action = action 
        self.parent = parent


class Frontier:
    def __init__(self):
        self.frontier =[]
        self.explored =[]

    def addNodes(self,node):
        self.frontier.append(node)

    def removeNode(self):
     node= self.frontier[0]
     self.frontier = self.frontier[1:]

     
     return node
    
    def exlploredNode(self,state):
        for cords in self.explored:
            if cords == state:
                return True

            
                
        return False 
        
   




    


        

        
        
