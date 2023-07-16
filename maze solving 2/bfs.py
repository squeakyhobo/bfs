import pygame 
pygame.init()
from functions import Node
from functions import Frontier








clock = pygame.time.Clock()


screen =pygame.display.set_mode((400,400))

test_surface = pygame.Surface((360,360))


player = pygame.Surface((40,40))
player_x = 40
player_y = 40

end_point = pygame.Surface((40,40))
end_point_coords  = (360,360)
frontier = Frontier()


start_node = Node((40,40),None,None)
   
        
frontier.addNodes(start_node) 
inFrontiter = False




test_surface.fill("red")
end_point.fill("green")
player.fill("white")
game = True
while game:
        
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        for i in range(40,360,40):
            pygame.draw.line(test_surface,(255,255,255),(i,0),(i,400),1)
            pygame.draw.line(test_surface,(255,255,255),(0,i),(400,i),1)

        
        screen.blit(test_surface,(40,40))
        screen.blit(end_point,end_point_coords)
        
        
        
        node = frontier.removeNode()
        
        explored = frontier.exlploredNode(node.state)
        if explored == True:
             print (explored)
        
        elif explored == False:
             screen.blit(player,node.state)
             player_x = node.state[0]
             player_y = node.state[1]
             frontier.explored.append(node.state)
             if node.state[0] == end_point_coords[0] and node.state[1] == end_point_coords[1]:
                  #parent finder 
                  print("done")
                  while node.parent is not None:
                        
                        node = node.parent
                        area= pygame.Rect(node.state[0],node.state[1],40,40)
                        screen.fill((0,255,0),area)
                        
                    
                  game= False
                        
                        
                  
             elif node.state[0] != end_point_coords[0] or node.state[1] != end_point_coords[1]:

                    above_ofr= (player_x,player_y-40)
                    below_ofr =(player_x,player_y+40)
                    forward_ofr=(player_x+40,player_y)
                    backwards_ofr=(player_x-40,player_x)
                    
                    if (node.state[0] >= 40 and node.state[0]<= 360)  and  (node.state[1] >= 40 and node.state[1]<= 360):
                         if (above_ofr[1] >= 40  and above_ofr[1]< 360)and (above_ofr[0]>= 40 and above_ofr[0]<=360):
                              node1 = Node(above_ofr,(0,-40),node)
                              for cords in frontier.frontier:
                                   if cords ==node1.state:   
                                        
                                        inFrontiter = True
                              if inFrontiter == False:
                                        frontier.addNodes(node=node1)
                              elif inFrontiter ==True:
                                   print ("already in frontier")
                                   inFrontiter = False
                         else:
                              print("not up ")
                              
                         if (below_ofr[1] <= 360 and below_ofr[1] >40 )and(below_ofr[0]>= 40 and below_ofr[0]<=360)  :
                              node1 = Node(below_ofr,(0,+40),node)
                              for cords in frontier.frontier:
                                   if cords ==node1.state:   
                                        
                                        inFrontiter = True
                              if inFrontiter == False:
                                        frontier.addNodes(node=node1)
                              elif inFrontiter ==True:
                                   print ("already in frontier")
                                   inFrontiter = False
                         else:
                              print("not down")
                         
                         if forward_ofr[0] <= 360 :
                              node1 = Node(forward_ofr,(40,0),node)
                              for cords in frontier.frontier:
                                   if cords ==node1.state:   
                                        
                                        inFrontiter = True
                              if inFrontiter == False:
                                        frontier.addNodes(node=node1)
                              elif inFrontiter ==True:
                                   print ("already in frontier")
                                   inFrontiter = False
                         else:
                          print("not forward ")
                              
                         if backwards_ofr[0] >= 40:
                              node1 = Node(above_ofr,(-40,0),node)
                              for cords in frontier.frontier:
                                   if cords ==node1.state:   
                                        
                                        inFrontiter = True
                              if inFrontiter == False:
                                        frontier.addNodes(node=node1)
                              elif inFrontiter ==True:
                                   print ("already in frontier")
                                   inFrontiter = False
                         else:
                              print("not backwardss ")

                        

             else:
                  print("error")
        else:
               print("error")    
        
        
            

        
        
        
        
        
        
        
        
        pygame.display.update()