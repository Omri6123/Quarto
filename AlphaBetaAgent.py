from Quarto import Quarto
from State import State
import numpy as np
from Constant import *
MAXSCORE = 1000

class AlphaBetaAgent:

    def __init__(self, player, depth, environment: Quarto = None):
        self.player = player
        self.depth = depth
        self.environment : Quarto = environment

    def evaluate (self, state : State): #CHECK IF WIN + 100 LOSE - 100 IF PIECE CAN END GAME -20
        score = 0
        piece = self.pieceIndex(state.Piece)

        colorboard = state.board[0]
        shapeboard = state.board[1]
        sizeboard = state.board[3]
        #COLOR - DONE
        row_sumcolor = np.sum(colorboard, axis=1) #
        rowcolor3W = (np.where(row_sumcolor==3))[0]
        rowcolor3B = np.where(row_sumcolor==-3)[0]
        diagonalscolor =np.trace(colorboard) #
        diagonalscolorflip = np.trace(np.fliplr(colorboard)) #
        diagonals3W = np.where(diagonalscolor==3)[0]
        diagonals3B= np.where(diagonalscolor==-3)[0]
        diagonalsflip3W= np.where(diagonalscolorflip==3)[0]
        diagonalsflip3B= np.where(diagonalscolorflip==-3)[0]
        col_sumcolor = np.sum(colorboard, axis=0)#
        colcolor3W = np.where(col_sumcolor==3)[0]
        colcolor3B = np.where(col_sumcolor==-3)[0]

        #SHAPE
        row_sumshape = np.sum(shapeboard, axis=1)#
        rowshape3W= np.where(row_sumshape==3)[0]
        rowshape3B= np.where(row_sumshape==-3)[0]
        diagonalsshape =np.trace(shapeboard) #
        diagonalsshapeflip = np.trace(np.fliplr(shapeboard)) #
        diagonalsshape3W = np.where(diagonalsshape==3)[0]
        diagonalsshape3B= np.where(diagonalsshape==-3)[0]
        diagonalsshapeflip3W= np.where(diagonalsshapeflip==3)[0]
        diagonalsshapeflip3B= np.where(diagonalsshapeflip==-3)[0]
        col_sumshape = np.sum(shapeboard, axis=0)#
        colshape3W= np.where(col_sumshape==3)[0]
        colshape3B=np.where(col_sumcolor==-3)[0]
        
        #SIZE
        row_sumsize = np.sum(sizeboard, axis=1)
        rowsize3W= np.where(row_sumsize==3)[0]
        rowsize3B= np.where(row_sumsize==-3)[0]
        diagonalssize =np.trace(sizeboard) #
        diagonalssizeflip = np.trace(np.fliplr(sizeboard)) #
        diagonalssize3W = np.where(diagonalssize==3)[0]
        diagonalssize3B= np.where(diagonalssize==-3)[0]
        diagonalssizeflip3W= np.where(diagonalssizeflip==3)[0]
        diagonalssizeflip3B= np.where(diagonalssizeflip==-3)[0]
        col_sumsize = np.sum(sizeboard, axis=0)#
        colsize3W= np.where(col_sumsize==3)[0]
        colsize3B=np.where(col_sumcolor==-3)[0]
        if self.environment.is_end_of_game(state):
            if state.end_of_game == 1 and self.player == state.player:
                return -100
            elif state.end_of_game == 1 and self.player != state.player:
                return 100
            elif state.end_of_game == 2:
                return 0

        if piece[0] == 1:
            if (l:=len(rowcolor3W))!=0:
                return 50
            if (l:=len(diagonals3W))!=0:
                return 50
            if (l:=len(diagonalsflip3W))!=0:
                return 50
            if (l:=len(colcolor3W))!=0:
                return 50
        elif piece[0] == -1:
            if (l:=len(rowcolor3B))!=0:
                return 50
            if (l:=len(diagonals3B))!=0:
                return 50
            if (l:=len(diagonalsflip3B))!=0:
                return 50
            if (l:=len(colcolor3B))!=0:
                return 50
        if piece[1] ==1:
            if (l:=len(rowshape3W))!=0:
                return 50
            if (l:=len(diagonalsshape3W))!=0:
                return 50
            if (l:=len(diagonalsshapeflip3W))!=0:
                return 50
            if (l:=len(colshape3W))!=0 :
                return 50
        elif piece[1] ==-1:
            if (l:=len(rowshape3B))!=0:
                return 50
            if (l:=len(diagonalsshape3B))!=0:
                return 50
            if (l:=len(diagonalsshapeflip3B))!=0:
                return 50
            if (l:=len(colshape3B))!=0 :
                return 50
        if piece[3] == 1:
            if (l:=len(rowsize3W))!=0:
                return 50
            if (l:=len(diagonalssize3W))!=0:
                return 50
            if (l:=len(diagonalssizeflip3W))!=0:
                return 50
            if (l:=len(colsize3W))!=0:
                return 50
        elif piece[3]==-1:
            if (l:=len(rowsize3B))!=0:
                return 50
            if (l:=len(diagonalssize3B))!=0:
                return 50
            if (l:=len(diagonalssizeflip3B))!=0:
                return 50
            if (l:=len(colsize3B))!=0:
                return 50

        #region COLOR
        if (l:=len(rowcolor3W))!=0 and ((c:=self.CountType(state.ListBool,0, 1)) != 0):
            score += l*c*-2
        if (l:=len(rowcolor3B))!=0 and ((c:=self.CountType(state.ListBool,0, -1)) != 0):
            score += l*c*-2
        if (l:=len(diagonals3W))!=0 and ((c:=self.CountType(state.ListBool,0, 1)) != 0):
            score += l*c*-2
        if (l:=len(diagonals3B))!=0 and ((c:=self.CountType(state.ListBool,0, -1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalsflip3W))!=0 and ((c:=self.CountType(state.ListBool,0, 1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalsflip3B))!=0 and ((c:=self.CountType(state.ListBool,0, -1)) != 0):
            score += l*c*-2
        if (l:=len(colcolor3W))!=0 and ((c:=self.CountType(state.ListBool,0, 1)) != 0):
            score += l*c*-2
        if (l:=len(colcolor3B))!=0 and ((c:=self.CountType(state.ListBool,0, -1)) != 0):
            score += l*c*-2
        #endregion
       
        #region SHAPE
        if (l:=len(rowshape3W))!=0 and ((c:=self.CountType(state.ListBool,1, 1)) != 0):
            score += l*c*-2
        if (l:=len(rowshape3B))!=0 and ((c:=self.CountType(state.ListBool,1, -1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalsshape3W))!=0 and ((c:=self.CountType(state.ListBool,1, 1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalsshape3B))!=0 and ((c:=self.CountType(state.ListBool,1, -1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalsshapeflip3W))!=0 and ((c:=self.CountType(state.ListBool,1, 1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalsshapeflip3B))!=0 and ((c:=self.CountType(state.ListBool,1, -1)) != 0):
            score += l*c*-2
        if (l:=len(colshape3W))!=0 and ((c:=self.CountType(state.ListBool,1, 1)) != 0):
            score += l*c*-2
        if (l:=len(colshape3B))!=0 and ((c:=self.CountType(state.ListBool,1, -1)) != 0):
            score += l*c*-2
        #endregion

        #region SIZE
        if (l:=len(rowsize3W))!=0 and ((c:=self.CountType(state.ListBool,3, 1)) != 0):
            score += l*c*-2
        if (l:=len(rowsize3B))!=0 and ((c:=self.CountType(state.ListBool,3, -1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalssize3W))!=0 and ((c:=self.CountType(state.ListBool,3, 1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalssize3B))!=0 and ((c:=self.CountType(state.ListBool,3, -1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalssizeflip3W))!=0 and ((c:=self.CountType(state.ListBool,3, 1)) != 0):
            score += l*c*-2
        if (l:=len(diagonalssizeflip3B))!=0 and ((c:=self.CountType(state.ListBool,3, -1)) != 0):
            score += l*c*-2
        if (l:=len(colsize3W))!=0 and ((c:=self.CountType(state.ListBool,3, 1)) != 0):
            score += l*c*-2
        if (l:=len(colsize3B))!=0 and ((c:=self.CountType(state.ListBool,3, -1)) != 0):
            score += l*c*-2
        #endregion

        return score

    def CountType(self, Listbool, type, typeint):
        count = 0
        for i in range(16):
            if Listbool[i] and pieceList[i][type]==typeint:
                count+=1
        return count

    def pieceIndex(self, piece):
        return pieceList[piece-1]
    
    def getAction(self, events=None,state: State=None, train=False):
        visited = set()
        value, bestAction = self.minMax(state, visited)
        return bestAction

    def minMax(self, state:State, visited:set):
        depth = 0
        alpha = -MAXSCORE
        beta = MAXSCORE
        return self.max_value(state, visited, depth, alpha, beta)
        
    def max_value (self, state:State, visited:set, depth, alpha, beta):
        
        value = -MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(state,action)
            if newState not in visited:
                visited.add(newState)
                newValue, newAction = self.min_value(newState, visited,  depth + 1, alpha, beta)
                if newValue > value:
                    value = newValue
                    bestAction = action
                    alpha = max(alpha, value)
                if value >= beta:
                    return value, bestAction
                    

        if bestAction:    
            return value, bestAction 
        else:               # happend when all child states are in visited. return maxScore
            return MAXSCORE, bestAction

    def min_value (self, state:State, visited:set, depth, alpha, beta):
        
        value = MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(state,action)
            if newState not in visited:
                visited.add(newState)
                newValue, newAction = self.max_value(newState, visited,  depth + 1, alpha, beta)
                if newValue < value:
                    value = newValue
                    bestAction = action
                    beta = min(beta, value)
                if value <= alpha:
                    return value, bestAction

        if bestAction:
            return value, bestAction 
        else:
            return -MAXSCORE, bestAction
 