"""Reverse-engineered client for snake.

This is an ASCII clone of the Snake game used in the Orbis Challenge 2014.
It should be capable of using files developed for Orbis Challenge 2014.

Game maps consist of the following elements:
WALL
LIGHTCYCLE
POWERUP
EMPTY
TRAIL

Lightcycle dictionary will consist of following data:


It will call the following function to obtain next move:

get_move(self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):

"""

#class Player:

import random
import PlayerActions
import time
import math
import PlayerAI
import Suicide
import os
import platform
class GameMap:
    
    def __init__(self):
        self.mapData=[]
        self.playerList = []#List of all players. Number 1 is always a meatbag, and all other are cold, unthinking soulless machines.
        return
    def RandomGameMap(self, wallDensity, xSize, ySize, startPosList, AIname):
        #Generate a randomized game map.
        for y in range(ySize):
            thisRow = []
            for x in range(xSize):
                noWall = 0
                for i in startPosList:
                    if ((abs(x - i[0])) <= 2) and ((abs(y - i[1])) <= 2):
                        noWall = 1;                    
                #All borders should be walls. In addition all player start locations should be free of walls.
                if (random.random() > wallDensity) and (not ((x == 0)or(x == (xSize-1)) or (y==0) or (y==(ySize-1)))):
                    thisRow.append("EMPTY")
                elif (noWall == 0) or (((x == 0)or(x == (xSize-1)) or (y==0) or (y==(ySize-1)))):
                    thisRow.append("WALL")
                else:
                    thisRow.append("EMPTY")
            self.mapData.append(thisRow)

                
    def LoadGameMapFromFile(self,filename,delimiter):
        #So I can load stuff from, say, a CSV file. Yay Excel is my Level editor!
        myfile = file.open(filename)
        myfile = myfile.read()
        myfile = myfile.split("\n")
        self.mapData = []
        for i in myfile:
            self.mapData.append(i.split(delimiter))

class PlayingField(GameMap):
    def InitializeMap(self, wallDensity, xSize, ySize, startPosList, AIname, PowerupSpawnChance):
        self.RandomGameMap(wallDensity, xSize, ySize, startPosList, AIname)
                #Now, we need to generate players. Create a player for each start pos, and the first
        #becomes the human's start pos.
        playerNumber = 0;#This gets set to 1 after first player (the human) is set.
        self.PowerupSpawnChance = PowerupSpawnChance#This thing lets us set our powerup spawn chance, duh. Every turn, this is the chance that a powerup will be spawned (randomly from the list of available powerups) on a random empty location on the map.
        for player in startPosList:
            if (playerNumber == 0):
                #Set the Human player.
                self.playerList.append(HumanPlayerObject(player, self))
            else:
                self.playerList.append(PlayerObject(AIname[playerNumber], player, self))
            playerNumber+=1
        #After initializing ppl, we set the appropriate locations to be filled with Lightcycles.
        for i in startPosList:
            thisLine = self.mapData[i[0]]
            thisLine[i[1]] = "LIGHTCYCLE"
            self.mapData[i[0]] = thisLine 
    def PrintMap(self):
        myString = ""
        for y in range(len(self.mapData)):
            for x in range(len(self.mapData[0])):
                #Print stuff out. "X" is a Wall, "O" is a Player, "." is a Floor, "~" is a Trail, "P" is a Powerup. 
                mapItem = self.mapData[y][x]
                if mapItem == "WALL":
                    myString += "X"
                elif mapItem=="LIGHTCYCLE":
                    myString += "@"
                elif mapItem=="EMPTY":
                    myString += " "
                elif mapItem=="TRAIL":
                    myString += "~"
                elif mapItem=="POWERUP" or mapItem=="POWERUP_MISSILE" or mapItem=="POWERUP_LASER" or mapItem=="POWERUP_BOMB" or mapItem=="POWERUP_INVINCIBILITY":
                    myString += "P"
            myString += "\n"
        return myString
    def findNearestPlayer(self, player):
        minDistance = len(self.mapData)+len(self.mapData[0])
        nearestPlayer = None;
        playerPosition = player.position;
        for i in self.playerList:
            difference = (player.position[0] - i.position[0], player.position[1] - i.position[1]);
            
            dist_mag = abs(pow(difference[0], 2) + pow(difference[1], 2))
            
            dist_mag = math.sqrt(abs(dist_mag));
            if dist_mag <= minDistance and dist_mag != 0 and i.isAlive:
                nearestPlayer = i;
                minDistance = dist_mag;
        #print nearestPlayer;
        #print minDistance;
        return nearestPlayer;
    def findNearestPlayerInclDead(self, player):
        minDistance = len(self.mapData)+len(self.mapData[0])
        nearestPlayer = None;
        playerPosition = player.position;
        for i in self.playerList:
            difference = (player.position[0] - i.position[0], player.position[1] - i.position[1]);
            
            dist_mag = abs(pow(difference[0], 2) + pow(difference[1], 2))
            
            dist_mag = math.sqrt(abs(dist_mag));
            if dist_mag <= minDistance and dist_mag != 0:
                nearestPlayer = i;
                minDistance = dist_mag;
        #print nearestPlayer;
        #print minDistance;
        return nearestPlayer;
            
            
    def next_step(self):
        #This will update the game by one step.
        #For each player, get the next move, and then update the board positions based on this.
        #Take the players' next moves, and move them around.
        #If a powerup is activated, then carry out its effects.
        #If a player is trying to move into a wall or trail, end the game (set its status to dead).
        #If a player is dead, then we don't update them any longer (and their lightcycle gets removed from the game).
        #print self.playerList
        for i in self.playerList:
            #Call their nextMove function, and use that with move_player to determine next position.
            #print i
            if i.isAlive:
                self.move_player(i, i.getNextMove())
        if (random.random() < self.PowerupSpawnChance):
            powerupPlaced = True
            while (powerupPlaced):
                #Select random space on board. 
                xcoord = random.choice(range(1, len(self.mapData[0])))
                ycoord = random.choice(range(1, len(self.mapData)))
                if self.mapData[xcoord][ycoord] == "EMPTY":
                    self.mapData[xcoord][ycoord] = "POWERUP"
                    powerupPlaced = False


    def move_player(self, player, direction):
        
        currPos = player.position
        
        if direction == PlayerActions.MOVE_UP:
            newPos = (currPos[0], currPos[1]-1)
        elif direction == PlayerActions.MOVE_DOWN:
            newPos = (currPos[0], currPos[1]+1)
        elif direction == PlayerActions.MOVE_LEFT:
            newPos = (currPos[0]-1, currPos[1])
        elif direction == PlayerActions.MOVE_RIGHT:
            newPos = (currPos[0]+1, currPos[1])
        elif direction == PlayerActions.ACTIVATE_POWERUP:
            self.activatePowerUp(player)
            newPos = currPos;
        elif direction == PlayerActions.ACTIVATE_POWERUP_MOVE_UP:
            newPos = (currPos[0], currPos[1]-1)
            self.activatePowerUp(player)
        elif direction == PlayerActions.ACTIVATE_POWERUP_MOVE_DOWN:
            newPos = (currPos[0], currPos[1]+1)
            self.activatePowerUp(player)
        elif direction == PlayerActions.ACTIVATE_POWERUP_MOVE_LEFT:
            newPos = (currPos[0]-1, currPos[1])
            self.activatePowerUp(player)
        elif direction == PlayerActions.ACTIVATE_POWERUP_MOVE_RIGHT:
            newPos = (currPos[0]+1, currPos[1])
            self.activatePowerUp(player)
        else:
            newPos = currPos
        #Now that we've got the direction, change the player's position, and
        #change the grid.

        if self.mapData[newPos[0]][newPos[1]] == "POWERUP":
            player.givePowerup()
        if (not (player.isMissile)):
            self.mapData[currPos[0]] [currPos[1]] = "TRAIL";
        else:
            self.mapData[currPos[0]] [currPos[1]] = "EMPTY";
        if self.mapData[newPos[0]][newPos[1]] == "WALL" or self.mapData[newPos[0]][newPos[1]] == "TRAIL": 
            player.isAlive = False;#Ur ded
        elif self.mapData[newPos[0]][newPos[1]] == "LIGHTCYCLE":
            self.mapData[newPos[0]] [newPos[1]] = "EMPTY";
            player.isAlive = False;#Ur ded
            for i in self.playerList:
                if i.position == (newPos[0], newPos[1]):
                    i.isAlive = False;
        else:
            self.mapData[newPos[0]] [newPos[1]] = "LIGHTCYCLE";
        

        
        player.position = newPos;
        player.direction = direction;
        
    def activatePowerUp(self, player):
        #This does some thing depending on the powerup we get.
        #Possible powerups are: INVINCIBILITY, BOMB and MISSILE.
        #MISSILE is a suicidal player that tries to crash into someone. (lol)
        pass
    
def getPlayerDict(player):
    
    return {"position":player.position, "powerupType":player.powerupType, "direction":player.direction, "hasPowerup":player.hasPowerup, "isInvincible":player.isInvincible}
class PlayerObject:
    #This class contains the player's position, and powerup status.
    #The actual game class contains a game map object, and one player object for each player.
    #HumanPlayerObject inherits from this class and uses human input to decide next move.
    def __init__(self, AImodule, position, parentObj):
        self.isAlive = True
        self.isMissile = False
        self.AIname = AImodule;
        self.position = position;
        self.powerupType = "NONE"
        self.direction = PlayerActions.MOVE_UP;
        self.hasPowerup = False;
        self.isInvincible = False;
        self.parentObj = parentObj;
        #Lightcycle dict: {"position":self.position, "powerupType":self.powerupType, "direction":self.direction, "hasPowerup":self.hasPowerup, "isInvincible":self.isInvincible}
    def givePowerup(self):
        #Give us a powerup.
        self.hasPowerup = True
        self.powerupType = random.choice(["BOMB"])
    def getNextMove(self):
        if self.AIname == "Machine":
            myAI = PlayerAI.PlayerAI()
        elif self.AIname == "Missile":
            myAI = Suicide.Suicide()
            #print self.parentObj.findNearestPlayer(self)
        else:
            myAI = PlayerAI.PlayerAI()
        #print "Mypos is:" 
        #print self.parentObj.findNearestPlayer(self).position
        enemyPlayer = self.parentObj.findNearestPlayer(self)
        if enemyPlayer != None:
            enemyPlayerDict = getPlayerDict(enemyPlayer)
        else:
            enemyPlayerDict = getPlayerDict(self.parentObj.findNearestPlayerInclDead(self))
        try:
            nextMove = myAI.get_move(self.parentObj.mapData, getPlayerDict(self), enemyPlayerDict, 0)
            return nextMove
        except:
            return self.direction
        #Execute the move.
        '''
        if nextMove == PlayerActions.MOVE_UP:
            self.moveUp()
        elif nextMove == PlayerActions.MOVE_DOWN:
            self.moveDown()
        elif nextMove == PlayerActions.MOVE_LEFT:
            self.moveLeft()
        elif nextMove == PlayerActions.MOVE_RIGHT:
            self.moveRight()
        elif nextMove == PlayerActions.ACTIVATE_POWERUP:
            self.activatePowerUp()
        elif nextMove == PlayerActions.ACTIVATE_POWERUP_MOVE_UP:
            self.activatePowerUp()
            self.moveUp()
        elif nextMove == PlayerActions.ACTIVATE_POWERUP_MOVE_DOWN:
            self.activatePowerUp()
            self.moveDown()
        elif nextMove == PlayerActions.ACTIVATE_POWERUP_MOVE_LEFT:
            self.activatePowerUp()
            self.moveLeft()
        elif nextMove == PlayerActions.ACTIVATE_POWERUP_MOVE_RIGHT:
            self.activatePowerUp()
            self.moveRight()       
            '''
class HumanPlayerObject(PlayerObject):#A player controlled by a meatbag.
    def __init__(self, position, parentObj):
        self.isAlive = True
        self.AIname = "Human";
        self.isMissile = False
        self.position = position;
        self.powerupType = "NONE"
        self.direction = PlayerActions.MOVE_UP;
        self.hasPowerup = False;
        self.isInvincible = False;
        self.parentObj = parentObj
    def runme(self):
        nextMove = self.human_get_move(self, self.parentObj.mapData, player_lightcycle, opponent_lightcycle, 0)#Requests key input from the fleshy meatbag sitting on the chair.
        return nextMove
    def getNextMove(self):
        return 0
    
if __name__ == "__main__":
    Midgard = PlayingField()
    Midgard.InitializeMap(0.1, 40, 40, [(1, 1), (1,2), (38, 38)], ["Human", "Machine", "Missile"], 0)
    Midgard.findNearestPlayer(Midgard.playerList[0])
    stillAlive = True
    myPlatform = platform.system()
    while (stillAlive):
        
        
        Midgard.next_step()
        myString = Midgard.PrintMap()
        if myPlatform == "Windows":
            #os.system("cls")
            pass
        elif myPlatform == "Linux":
            os.system("clear")
        print myString
        time.sleep(0.05)
        stillAlive = False
        for i in Midgard.playerList:
            #Call their nextMove function, and use that with move_player to determine next position.
            
            if i.isAlive:
                stillAlive = True
    print "Game over"
    endGame = raw_input("Press Enter to close")
    

