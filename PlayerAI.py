'''

AI for team AdvancedPersistentThreat for the 2014 Orbis Challenge
Made the top 10!



'''
import random
import timeit
import time
import PlayerActions
WALL = "WALL"
LIGHTCYCLE = "LIGHTCYCLE"
TRAIL = "TRAIL"
POWERUP = "POWERUP"
class PlayerAI():
    def __init__(self):
        return

    def new_game(self, game_map, player_lightcycle, opponent_lightcycle):
        return

    def available_moves(self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        up = 0
        right = 1
        down = 2
        left = 3

        my_position = player_lightcycle['position']
        my_x = my_position[0]
        my_y = my_position[1]
        my_direction = player_lightcycle['direction']

        blow_moves = [] # moves if powerup is used for survival

        if my_direction == left:
            ok_moves = [left,up,down]
            if game_map[my_x-1][my_y] == WALL or game_map[my_x-1][my_y] == LIGHTCYCLE or game_map[my_x-2][my_y] == LIGHTCYCLE or game_map[my_x-1][my_y] == TRAIL:
                ok_moves.remove(left)
            if game_map[my_x][my_y-1] == WALL or game_map[my_x][my_y-1] == LIGHTCYCLE or game_map[my_x][my_y-2] == LIGHTCYCLE or game_map[my_x][my_y-1] == TRAIL:
                ok_moves.remove(up)
            if game_map[my_x][my_y+1] == WALL or game_map[my_x][my_y+1] == LIGHTCYCLE or game_map[my_x][my_y+2] == LIGHTCYCLE or game_map[my_x][my_y+1] == TRAIL:
                ok_moves.remove(down)

            if len(ok_moves) == 0:
                if game_map[my_x-1][my_y] != WALL:
                    blow_moves.append(left)
                if game_map[my_x][my_y-1] != WALL:
                    blow_moves.append(up)
                if game_map[my_x][my_y+1] != WALL:
                    blow_moves.append(down)

        elif my_direction == right:
            ok_moves = [right,up,down]
            if game_map[my_x+1][my_y] == WALL or game_map[my_x+1][my_y] == LIGHTCYCLE or game_map[my_x+2][my_y] == LIGHTCYCLE or game_map[my_x+1][my_y] == TRAIL:
                ok_moves.remove(right)
            if game_map[my_x][my_y-1] == WALL or game_map[my_x][my_y-1] == LIGHTCYCLE or game_map[my_x][my_y-2] == LIGHTCYCLE or game_map[my_x][my_y-1] == TRAIL:
                ok_moves.remove(up)
            if game_map[my_x][my_y+1] == WALL or game_map[my_x][my_y+1] == LIGHTCYCLE or game_map[my_x][my_y+2] == LIGHTCYCLE or game_map[my_x][my_y+1] == TRAIL:
                ok_moves.remove(down)

            if len(ok_moves) == 0:
                if game_map[my_x+1][my_y] != WALL:
                    blow_moves.append(right)
                if game_map[my_x][my_y-1] != WALL:
                    blow_moves.append(up)
                if game_map[my_x][my_y+1] != WALL:
                    blow_moves.append(down)

        elif my_direction == up:
            ok_moves = [up, left,right]
            if game_map[my_x-1][my_y] == WALL or game_map[my_x-1][my_y] == LIGHTCYCLE or game_map[my_x-2][my_y] == LIGHTCYCLE or game_map[my_x-1][my_y] == TRAIL:
                ok_moves.remove(left)
            if game_map[my_x+1][my_y] == WALL or game_map[my_x+1][my_y] == LIGHTCYCLE or game_map[my_x+2][my_y] == LIGHTCYCLE or game_map[my_x+1][my_y] == TRAIL:
                ok_moves.remove(right)
            if game_map[my_x][my_y-1] == WALL or game_map[my_x][my_y-1] == LIGHTCYCLE or game_map[my_x][my_y-2] == LIGHTCYCLE or game_map[my_x][my_y-1] == TRAIL:
                ok_moves.remove(up)

            if len(ok_moves) == 0:
                if game_map[my_x][my_y-1] != WALL:
                    blow_moves.append(up)
                if game_map[my_x-1][my_y] != WALL:
                    blow_moves.append(left)
                if game_map[my_x+1][my_y] != WALL:
                    blow_moves.append(right)

        else:
            ok_moves = [down,left,right]
            if game_map[my_x-1][my_y] == WALL or game_map[my_x-1][my_y] == LIGHTCYCLE or game_map[my_x-2][my_y] == LIGHTCYCLE or game_map[my_x-1][my_y] == TRAIL:
                ok_moves.remove(left)
            if game_map[my_x+1][my_y] == WALL or game_map[my_x+1][my_y] == LIGHTCYCLE or game_map[my_x+2][my_y] == LIGHTCYCLE or game_map[my_x+1][my_y] == TRAIL:
                ok_moves.remove(right)
            if game_map[my_x][my_y+1] == WALL or game_map[my_x][my_y+1] == LIGHTCYCLE or game_map[my_x][my_y+2] == LIGHTCYCLE or game_map[my_x][my_y+1] == TRAIL:
                ok_moves.remove(down)

            if len(ok_moves) == 0:
                if game_map[my_x][my_y-1] != WALL:
                    blow_moves.append(down)
                if game_map[my_x-1][my_y] != WALL:
                    blow_moves.append(left)
                if game_map[my_x+1][my_y] != WALL:
                    blow_moves.append(right)

        available_moves = {'ok_moves':ok_moves, 'blow_moves':blow_moves}
        return available_moves



    def wall_hug(self, moves):
        return moves[0]

    def get_move(self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        #tic = timeit.default_timer()

        # matching direction to numbers
        up = 0
        right = 1
        down = 2
        left = 3

        my_position = player_lightcycle['position']
        my_x = my_position[0]
        my_y = my_position[1]
        my_direction = player_lightcycle['direction']

        available_moves = self.available_moves(game_map, player_lightcycle, opponent_lightcycle, moveNumber)
        ok_moves = available_moves['ok_moves']
        blow_moves = available_moves['blow_moves']

        #toc = timeit.default_timer()
        ##print 'This move took ' + str(tic-toc) + ' sec'
        #print "CURRENT POS: "
        #print my_position

        if len(ok_moves) > 0:
            nextMove = self.think(game_map, player_lightcycle, opponent_lightcycle, moveNumber)
            return nextMove
            if nextMove == up:
                return PlayerActions.MOVE_UP
            elif nextMove == right:
                return PlayerActions.MOVE_RIGHT
            elif nextMove == down:
                return PlayerActions.MOVE_DOWN
            else:
                return PlayerActions.MOVE_LEFT

        else: #won't work if my powerup is landmine
            nextMove = self.wall_hug(blow_moves)
            if nextMove == up:
                return PlayerActions.ACTIVATE_POWERUP_MOVE_UP
            elif nextMove == right:
                return PlayerActions.ACTIVATE_POWERUP_MOVE_RIGHT
            elif nextMove == down:
                return PlayerActions.ACTIVATE_POWERUP_MOVE_DOWN
            else:
                return PlayerActions.ACTIVATE_POWERUP_MOVE_LEFT

    def think(self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        my_position = player_lightcycle['position']
        their_position = opponent_lightcycle['position']
        data = time.time()
        mymap = self.graphify_exclude_ls(game_map)
        mymap = self.gridtograph(mymap)

            
        distance_to_target = self.bfs(mymap,my_position, opponent_lightcycle['position'], 75)
        distance_to_powerup = self.bfs_powerup(mymap,my_position, 75, game_map)
        their_distance_to_powerup = self.bfs_powerup(mymap,their_position, 75, game_map)

	#their_crowdedness = self.getOpenness(mymap, their_position, 100)
	#my_crowdedness = self.getOpenness(mymap, my_position, 100)


        #Can we get a powerup? If so, Fetch!
        if not (player_lightcycle['hasPowerup']) and(len(distance_to_powerup) > 0 and (len(their_distance_to_powerup) == 0 or len(distance_to_powerup) > len(their_distance_to_powerup))):
            #print "ADVANCE"                   
            return self.TACTIC_FOLLOW_PATH(distance_to_powerup, player_lightcycle, opponent_lightcycle, moveNumber)

            #Kill!

        #if their_crowdedness < 100 and my_crowdedness < 100 and (len(distance_to_target) < 6) and len(distance_to_target) != 0:
        #    #print "TERMINATE"
        #    return self.TACTIC_ORACLE(game_map, player_lightcycle, opponent_lightcycle, moveNumber)
        ##print len(distance_to_target)
        if len(distance_to_target) < 6  and len(distance_to_target) != 0:
            #print "THREATEN"
            return self.TACTIC_ORACLE_LITE_OFFENSIVE(game_map, player_lightcycle, opponent_lightcycle, moveNumber)
        #DEFAULT: Find most open space.
        #print "PERSIST"
        return self.TACTIC_MOST_OPEN_SPACE(game_map, player_lightcycle, opponent_lightcycle, moveNumber)
    
    def tupleAdd(self, tuple1, tuple2):
        return tuple(map(sum,zip(tuple1, tuple2)))
    
    def getOpenness(self, adjGraph, theRoot, maxsize = 100):
        #Given the GRAPH and the SPACE, find out how many places are SAFE.
        if not (theRoot in adjGraph):
            return []
        myqueue = []
        mySet = []
        mySet.append(theRoot)
        myqueue.append(theRoot)
        value = 0
        traversed = []
        while len(myqueue) > 0 and value < maxsize:
            t = myqueue [0]
            myqueue = myqueue[1:]
            value+=1
                
            for i in adjGraph[t]:
                if not(i in mySet):
                    mySet.append(i)
                    myqueue.append(i)
        return mySet

    def bfs(self, adjGraph, theRoot, theTarget, size):
        #Give us a PATH.
        if not (theRoot in adjGraph):
            return []
        myqueue = []
        mySet = []
        previous = {}
        mySet.append(theRoot)
        myqueue.append(theRoot)
        value = 0
        traversed = []
        while len(myqueue) > 0 and value < size and not (theTarget in mySet):
            t = myqueue [0]
            myqueue = myqueue[1:]
            value+=1
                
            for i in adjGraph[t]:
                if not(i in mySet):
                    mySet.append(i)
                    previous[i] = t
                    myqueue.append(i)

        path = []
        pathfinder = theTarget
        while pathfinder in previous:
            path.append(pathfinder)
            #print pathfinder
            pathfinder = previous[pathfinder]
        path.reverse()  

        return path
        
    def bfs_powerup(self, adjGraph, theRoot, size, theMap):
        #Give us a PATH to nearest powerup
        if not (theRoot in adjGraph):
            return []
        myqueue = []
        mySet = []
        previous = {}
        mySet.append(theRoot)
        myqueue.append(theRoot)
        value = 0
        traversed = []
        theTarget = 0
        while len(myqueue) > 0 and value < size and not theTarget:
            t = myqueue [0]
            myqueue = myqueue[1:]

            value+=1
            if theMap[t[0]][t[1]] == POWERUP:
                theTarget = t
            for i in adjGraph[t]:
                if not(i in mySet):
                    mySet.append(i)
                    previous[i] = t
                    myqueue.append(i)

        path = []
        pathfinder = theTarget
        while pathfinder in previous:
            path.append(pathfinder)
            
            pathfinder = previous[pathfinder]
        path.reverse()  
        return path

    def pathGenerator(self, adjMtx, root, depth):
        #Obtain a graph of up to distance DEPTH.
        newAdjMtx = {}
        if depth <= 0:
            return adjMtx[root]
        for i in adjMtx[root]:
            newAdjMtx[i] = self.pathGenerator(adjMtx, i, depth-1)
        return newAdjMtx
         
    def paths_calculateCost(self, paths):
            
        for i in paths:
            paths_calculate_cost(self, paths[i])
            if paths[i] == i:
                return 
            else:
                pass
            #For each value in paths, 
    
    def whichWay(self, path, root):
        nextStep = path[0]
	#print (-root[0]+nextStep[0], -root[1]+nextStep[1])
        if self.tupleAdd(root, (-1, 0)) == nextStep:#up
            return PlayerActions.MOVE_LEFT
        elif self.tupleAdd(root, (1, 0)) == nextStep:#down
            return PlayerActions.MOVE_RIGHT
        elif self.tupleAdd(root, (0, -1)) == nextStep:#left
            return PlayerActions.MOVE_UP
        elif self.tupleAdd(root, (0, 1)) == nextStep:#right
            return PlayerActions.MOVE_DOWN

    def TACTIC_ORACLE_LITE_OFFENSIVE (self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        my_position = player_lightcycle['position']
        their_position = opponent_lightcycle['position']
        mymap = self.graphify(game_map, my_position)
        mymap = self.gridtograph(mymap)
        
        mymap2 = self.graphify_exclude_root(game_map)
        mymap2 = self.gridtograph(mymap2)
            
        openSpaceLeft = {}
        nextSteps = mymap[my_position]
        for i in nextSteps:
            openSpaceLeft[i] = len(self.getOpenness(mymap2, i))
            stageTwo = self.graphify_exclude_positions(game_map, [my_position])#Evaluate opponent's next moves.
            stageTwo = self.gridtograph(stageTwo)
                
            enemy_nextSteps = stageTwo[their_position]

            for j in enemy_nextSteps:
                #openSpaceLeft[i] = openSpaceLeft[i] - (len(self.getOpenness(stageTwo, j))/2)
                stageTee = self.graphify_exclude_positions(game_map, [my_position, j])#Evaluate opponent's next moves.
                stageTee = self.gridtograph(stageTee)
                

                openSpaceLeft[i] = openSpaceLeft[i] + (len(self.getOpenness(stageTee, i)))
                if j == i:
                    openSpaceLeft[i] = openSpaceLeft[i] - 5000#We want to survive!!




        currOpenSpace = -999999
        for i in openSpaceLeft:
            if openSpaceLeft[i] > currOpenSpace:
                nextStep = i
                currOpenSpace = openSpaceLeft[i]
        if currOpenSpace == -999999:
            nextStep = random.shuffle(nextSteps)[0]
        #print nextStep
            
        return self.whichWay([nextStep],my_position)

    def TACTIC_ORACLE_LITE_DEFENSIVE (self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        my_position = player_lightcycle['position']
        their_position = opponent_lightcycle['position']
        mymap = self.graphify(game_map, my_position)
        mymap = self.gridtograph(mymap)
        
        mymap2 = self.graphify_exclude_root(game_map)
        mymap2 = self.gridtograph(mymap2)
        
        openSpaceLeft = {}
        nextSteps = mymap[my_position]
        for i in nextSteps:
            openSpaceLeft[i] = len(self.getOpenness(mymap2, i))
            stageTwo = self.graphify_exclude_positions(game_map, [i, my_position])#Evaluate opponent's next moves.
            stageTwo = self.gridtograph(stageTwo)
                
            enemy_nextSteps = stageTwo[their_position]
            enemyOpenSpaceLeft = {}
            for j in enemy_nextSteps:
                enemyOpenSpaceLeft[j] = len(self.getOpenness(stageTwo, j))
            currEnemyOpenSpace = -999999

            for l in enemyOpenSpaceLeft:
                if enemyOpenSpaceLeft[l] > currEnemyOpenSpace:
                    enemyNextStep = l
                    currEnemyOpenSpace = enemyOpenSpaceLeft[l]

            stageThree = self.graphify_exclude_positions(game_map, [enemyNextStep, my_position])#Evaluate opponent's next moves.
            stageThree = self.gridtograph(stageThree)
            my_nextSteps = stageThree[i]
            for k in my_nextSteps: openSpaceLeft[i] = openSpaceLeft[i] + len(self.getOpenness(stageThree, k))
        
        
        currOpenSpace = -999999
        for i in openSpaceLeft:
            if openSpaceLeft[i] > currOpenSpace:
                nextStep = i
                currOpenSpace = openSpaceLeft[i]
        if currOpenSpace == -999999:
            nextStep = random.shuffle(nextSteps)[0]
        #print openSpaceLeft
            
        return self.whichWay([nextStep],my_position)


    def TACTIC_ORACLE (self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        my_position = player_lightcycle['position']
        their_position = opponent_lightcycle['position']
        mymap = self.graphify(game_map, my_position)
        mymap = self.gridtograph(mymap)
        
        mymap2 = self.graphify_exclude_root(game_map)
        mymap2 = self.gridtograph(mymap2)
            
        openSpaceLeft = {}
        nextSteps = mymap[my_position]
        for i in nextSteps:
            openSpaceLeft[i] = len(self.getOpenness(mymap2, i))
            stageTwo = self.graphify_exclude_positions(game_map, [i, my_position])#Evaluate opponent's next moves.
            stageTwo = self.gridtograph(stageTwo)
                
            enemy_nextSteps = stageTwo[their_position]
            for j in enemy_nextSteps:
                openSpaceLeft[i] = openSpaceLeft[i] - len(self.getOpenness(stageTwo, j))
                stageThree = self.graphify_exclude_positions(game_map, [j, my_position])#Evaluate opponent's next moves.
                stageThree = self.gridtograph(stageThree)
            
                my_nextSteps = stageThree[i]
                for k in my_nextSteps: openSpaceLeft[i] = openSpaceLeft[i] + len(self.getOpenness(stageThree, k))
    
    
        currOpenSpace = -999999
        for i in openSpaceLeft:
            if openSpaceLeft[i] > currOpenSpace:
                nextStep = i
                currOpenSpace = openSpaceLeft[i]
        if currOpenSpace == -999999:
            nextStep = random.shuffle(nextSteps)[0]
        #print openSpaceLeft
            
        return self.whichWay([nextStep],my_position)
                    
                    
    def TACTIC_MOST_OPEN_SPACE (self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        my_position = player_lightcycle['position']
        mymap = self.graphify(game_map, my_position)
        mymap = self.gridtograph(mymap)
         
        mymap2 = self.graphify_exclude_root(game_map)
        mymap2 = self.gridtograph(mymap2)
            
        openSpaceLeft = {}
        nextSteps = mymap[my_position]
        for i in nextSteps:
            openSpaceLeft[i] = len(self.getOpenness(mymap2, i))
        currOpenSpace = 0
        for i in openSpaceLeft:
            if openSpaceLeft[i] > currOpenSpace:
                nextStep = i
                currOpenSpace = openSpaceLeft[i]
        if currOpenSpace == 0:
            nextStep = random.shuffle(nextSteps)[0]
	#print openSpaceLeft
        #print nextStep
        return self.whichWay([nextStep],my_position)
                
    def TACTIC_FOLLOW_PATH (self, path, player_lightcycle, opponent_lightcycle, moveNumber):
        #Just for fun.
        my_position = player_lightcycle['position']

            

        ##print myPath
        nextStep = self.whichWay(path, my_position)
        #print nextStep
        return nextStep


    def TACTIC_KAMIKAZE (self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        #Just for fun.
        my_position = player_lightcycle['position']
        mymap = self.graphify_whitelist(game_map, [my_position, opponent_lightcycle['position']])
        mymap = self.gridtograph(mymap)
        #print mymap[my_position]
        myPath = self.bfs(mymap,my_position, opponent_lightcycle['position'], 1000)
        

        ##print myPath
        nextStep = self.whichWay(myPath, my_position)
        return nextStep
            
    
            
    def minimax(self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        #For each possible path, compute how good the direction is.
        #Depth of 3.
        my_position = player_lightcycle['position']
        mymap = self.graphify(game_map,my_position)
        mymap = self.gridtograph(mymap)
        paths = self.pathGenerator(mymap, my_position, 3)
        #For each path, calculate the cost.
            
            

    def TACTIC_WALLHUG(self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
            
        NumORDER = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ORDER = {(0,-1):PlayerActions.MOVE_UP, (0,1):PlayerActions.MOVE_DOWN, (-1,0):PlayerActions.MOVE_LEFT, (1,0):PlayerActions.MOVE_RIGHT}
            
        random.shuffle(NumORDER)
        my_position = player_lightcycle['position']
        mymap = self.graphify(game_map,my_position)
        mymap = self.gridtograph(mymap)
        myDecision = 0
        myBad = 0
        #print self.getOpenness(mymap, my_position)

            
        for i in NumORDER:
            dest = tuple(map(sum,zip(my_position, i)))
            if self.isPassable(game_map, dest):
                adj = [self.tupleAdd(my_position, (-1, 0)), self.tupleAdd(my_position, (0, -1)), self.tupleAdd(my_position, (0, 1)), self.tupleAdd(my_position, (1, 0))]
                if any(self.isPassable(game_map, thePos) for thePos in adj):
                    myBad = i
                    myDecision = ORDER[i]



        return myDecision
                    
                            
        ''' COMMON FUNCTIONS'''
                
    def isPassable(self, game_map, dest):
        theX = int(dest[0])
        theY = int(dest[1])
        cell = game_map[theX][theY]
        if (cell == WALL) | (cell == TRAIL) |(cell == LIGHTCYCLE):
            return 0
        else:
            return 1
                
    def graphify(self, mymap, mypos):
        ylen = len(mymap)
        xlen = len(mymap[0])
        newmap = [0]*ylen
        for i in range(ylen):
            newmap[i] = [0]*xlen
        for x in range(ylen):
            for y in range(xlen):
                cell = mymap[x][y]
                if self.isPassable(mymap, (x,y)) or ((x, y)==mypos) :
                    newmap[x][y] = 1
                else:
                    newmap[x][y] = 0
        #The above will turn the mymap into a list of 1's and 0's.
        #No explosions, since those tiles would disappear after the turn.
        return newmap

    def graphify_whitelist(self, mymap, mypos):
        ylen = len(mymap)
        xlen = len(mymap[0])
        newmap = [0]*ylen
        for i in range(ylen):
            newmap[i] = [0]*xlen
        for x in range(ylen):
            for y in range(xlen):
                cell = mymap[x][y]
                if self.isPassable(mymap, (x,y)) or ((x, y) in mypos) :
                    newmap[x][y] = 1
                else:
                    newmap[x][y] = 0
        #The above will turn the mymap into a list of 1's and 0's.
        #No explosions, since those tiles would disappear after the turn.
        return newmap

    def graphify_exclude_root(self, mymap):
        ylen = len(mymap)
        xlen = len(mymap[0])
        newmap = [0]*ylen
        for i in range(ylen):
            newmap[i] = [0]*xlen
        for x in range(ylen):
            for y in range(xlen):
                cell = mymap[x][y]
                if self.isPassable(mymap, (x,y)):
                    newmap[x][y] = 1
                else:
                    newmap[x][y] = 0
        #The above will turn the mymap into a list of 1's and 0's.
        #No explosions, since those tiles would disappear after the turn.
        return newmap

    def graphify_exclude_ls(self, mymap):
        ylen = len(mymap)
        xlen = len(mymap[0])
        newmap = [0]*ylen
        for i in range(ylen):
            newmap[i] = [0]*xlen
        for x in range(ylen):
            for y in range(xlen):
                cell = mymap[x][y]
                if not((cell == WALL) | (cell == TRAIL) ):
                    newmap[x][y] = 1
                else:
                    newmap[x][y] = 0
        #The above will turn the mymap into a list of 1's and 0's.
        #No explosions, since those tiles would disappear after the turn.
        return newmap

    def graphify_exclude_positions(self, mymap, excluded):
        ylen = len(mymap)
        xlen = len(mymap[0])
        newmap = [0]*ylen
        for i in range(ylen):
            newmap[i] = [0]*xlen
        for x in range(ylen):
            for y in range(xlen):
                cell = mymap[x][y]
                if not((cell == WALL) | (cell == TRAIL) or ((x,y) in excluded)):
                    newmap[x][y] = 1
                else:
                    newmap[x][y] = 0
        #The above will turn the mymap into a list of 1's and 0's.
        #No explosions, since those tiles would disappear after the turn.
        return newmap

    def gridtograph(self, mymap):
        adjdict = {}#Adjacency dict is comprised 
        xlen = len(mymap)
        ylen = len(mymap[0])
        for x in range(xlen):
            for y in range(ylen):
                myspace = mymap[x][y]
                adjacents = []
                        
                if myspace !=0:
                    if (x+1) < xlen:
                        rightclear = mymap[x+1][y]
                        if rightclear:
                            adjacents.append((x+1, y))
                    else:
                        rightclear = 0

                    if (x-1) >= 0:
                        leftclear = mymap[x-1][y]
                        if leftclear:
                            adjacents.append((x-1, y))
                    else:
                        leftclear = 0
                                        
                    if (y+1) < ylen:
                        downclear = mymap[x][y+1]
                        if downclear:
                            adjacents.append((x, y+1))
                    else:
                        downclear = 0

                    if (y-1) > 0:
                        upclear = mymap[x][y-1]
                        if upclear:
                            adjacents.append((x, y-1))
                    else:
                        upclear = 0
                else: 
                    rightclear = 0
                    leftclear = 0
                    downclear = 0
                    upclear = 0
                    
                adjdict[(x,y)] = adjacents
        return adjdict




'''

8888888 8888888888 8 888888888o.      ,o888888o.     b.             8 
      8 8888       8 8888    `88.  . 8888     `88.   888o.          8 
      8 8888       8 8888     `88 ,8 8888       `8b  Y88888o.       8 
      8 8888       8 8888     ,88 88 8888        `8b .`Y888888o.    8 
      8 8888       8 8888.   ,88' 88 8888         88 8o. `Y888888o. 8 
      8 8888       8 888888888P'  88 8888         88 8`Y8o. `Y88888o8 
      8 8888       8 8888`8b      88 8888        ,8P 8   `Y8o. `Y8888 
      8 8888       8 8888 `8b.    `8 8888       ,8P  8      `Y8o. `Y8 
      8 8888       8 8888   `8b.   ` 8888     ,88'   8         `Y8o.` 
      8 8888       8 8888     `88.    `8888888P'     8            `Yo
      
                                Quick Guide
                --------------------------------------------
                      Feel free to delete this comment.

        1. THIS IS THE ONLY .PY OR .BAT FILE YOU SHOULD EDIT THAT CAME FROM THE ZIPPED STARTER KIT

        2. Any external files should be accessible from this directory

        3. new_game is called once at the start of the game if you wish to initialize any values

        4. get_move is called for each turn the game goes on

        5. game_map is a 2-d array that contains values for every board position.
                example call: game_map[2][3] == POWERUP would evaluate to True if there was a powerup at (2, 3)

        6. player_lightcycle is your lightcycle and is what the turn you respond with will be applied to.
                It is a dictionary with corresponding keys: "position", "direction", "hasPowerup", "isInvincible", "powerupType"
                position is a 2-element int array representing the x, y value
                direction is the direction you are travelling in. can be compared with Direction.DIR where DIR is one of UP, RIGHT, DOWN, or LEFT
                hasPowerup is a boolean representing whether or not you have a powerup
                isInvincible is a boolean representing whether or not you are invincible
                powerupType is what, if any, powerup you have

        7. opponent_lightcycle is your opponent's lightcycle. Same keys and values as player_lightcycle

        8. You ultimately are required to return one of the following:
                                                PlayerAction.SAME_DIRECTION
                                                PlayerAction.MOVE_UP
                                                PlayerAction.MOVE_DOWN
                                                PlayerAction.MOVE_LEFT
                                                PlayerAction.MOVE_RIGHT
                                                PlayerAction.ACTIVATE_POWERUP
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_UP
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_DOWN
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_LEFT
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_RIGHT
                
        9. If you have any questions, contact challenge@orbis.com

        10. Good luck! Submissions are due Sunday, September 21 at noon. You can submit multiple times and your most recent submission will be the one graded.
 
'''
