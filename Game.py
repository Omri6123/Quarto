import numpy as np
import pygame
from Graphics import Graphics
from Constant import *
from State import State
from Quarto import Quarto
import random
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from MinMaxAgent import MinMaxAgent
from AlphaBetaAgent import AlphaBetaAgent
from DQN_Agent import DQN_Agent
import time

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
graphics = Graphics()
pygame.display.update()
env = Quarto()
player1 = None
player2 = None

def main(player1, player2):
   
    player1=player1
    player2=player2
    run = True
    clock = pygame.time.Clock()
    graphics = Graphics()
    pygame.display.update()
    player = player1

    while(run):
        graphics.DrawBoard(env.state)
        pygame.display.update()
        
        clock.tick(FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
               break
        action = player.getAction(events=events, state=env.state)
        if action:
            env.move(state=env.state, action=action)
            graphics.DrawBoard(env.state)
            pygame.display.update()
            if env.is_end_of_game(env.state):
                if env.state.end_of_game == 1:
                    graphics.Win(state=env.state)
                    pygame.display.update()
                    env.state.setPiece(*action[0],action[1])
                    env.state = env.startState()
                    print(player.player, "Win")
                elif env.state.end_of_game == 2:
                    graphics.Draw(state=env.state)
                    pygame.display.update()
                    env.state.setPiece(*action[0],action[1])
                    env.state = env.startState()
                    print("Draw!")
                pygame.time.delay(8000)
                player = player1
                continue

            if player == player1:
                player = player2
            else:
                player = player1
               
        time.sleep(0.02)

    pygame.quit()

def GUI ():
    global player1, player2
    player1 = Human_Agent(player=1,graphics=graphics, env=env)
    player2 = Human_Agent(player=-1,graphics=graphics, env=env)
    # player1 = MinMaxAgent(player = 1,depth = 3, environment=env)
    # player2 = MinMaxAgent(player = -1,depth = 3, environment=env)
    # player1 = AlphaBetaAgent(player = 1,depth = 3, environment=env)
    # player2 = AlphaBetaAgent(player = -1,depth = 3, environment=env)
    # player1 = RandomAgent(player=1, env=env)
    # player2 = RandomAgent(player= -1, env=env)

    #player1 = DQN_Agent(env=env, player=1, parametes_path='Data/checkpoint1.pth', train=False)
    #player2 = DQN_Agent(env=env, player=-1, parametes_path='Data/checkpoint1.pth', train=False)

    player1_chosen = 0
    player2_chosen = 0
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 530<pos[0]<730 and 450<pos[1]<500:
                    main(player1, player2) 
                if 300<pos[0]<520 and 210<pos[1]<255:
                    player1 = Human_Agent(player=1,graphics=graphics, env=env)
                    player1_chosen=0
                if 730<pos[0]<850 and 210<pos[1]<255:
                    player2 = Human_Agent(player=-1,graphics=graphics, env=env)
                    player2_chosen=0
                if 300<pos[0]<520 and 265<pos[1]<310:
                    player1 = Random_Agent(player = 1, env=env)
                    player1_chosen=1
                if 730<pos[0]<850 and 265<pos[1]<310:
                    player2 = Random_Agent(player = -1, env=env)
                    player2_chosen=1
                if 300<pos[0]<520 and 320<pos[1]<365:
                    player1 = MinMaxAgent(player = 1,depth = 2, environment=env)
                    player1_chosen=2
                if 730<pos[0]<850 and 320<pos[1]<365:
                    player2 = MinMaxAgent(player = -1,depth = 2, environment=env)
                    player2_chosen=2
                if 300<pos[0]<520 and 375<pos[1]<410:
                    player1 = AlphaBetaAgent(player = 1,depth = 2, environment=env)
                    player1_chosen=3
                if 730<pos[0]<850 and 375<pos[1]<410:
                    player2 = AlphaBetaAgent(player = -1,depth = 2, environment=env)
                    player2_chosen=3
                if 300<pos[0]<520 and 420<pos[1]<465:
                    player1 = DQN_Agent(env=env, player=1, parametes_path='Data/checkpoint1.pth', train=False)
                    player1_chosen=4
                if 730<pos[0]<850 and 420<pos[1]<465:
                    player2 = DQN_Agent(env=env, player=-1, parametes_path='Data/checkpoint1.pth', train=False)
                    player2_chosen=4



        colors = [['gray','gray', 'gray', 'gray', 'gray'], ['gray','gray', 'gray', 'gray', 'gray']]
        colors[0][player1_chosen]=(205, 141, 29)
        colors[1][player2_chosen]=(205, 141, 29)

        TextFont = pygame.font.SysFont("Segoe Print", 70)
        TextFontP= pygame.font.SysFont("Segoe Print", 35)

        win.fill(BGCOLOR)
        TextHeader = TextFont.render("Quarto", 1, (26, 26, 26))
        TextName = TextFontP.render("Omri Benishay", 1, (26, 26, 26))
        win.blit(TextHeader, (500,45))
        win.blit(TextName, (492,125))

        write(win, 'Player 1',(320 ,150),color=BLACK)
        pygame.draw.rect(win, colors[0][0], (300,220,230,40),0,3)
        write(win, 'Human', (330,200),color=BLACK)
        pygame.draw.rect(win, colors[0][1], (300,270,230,40),0,3)
        write(win, 'Random', (315,250),color=BLACK)
        pygame.draw.rect(win, colors[0][2], (300,320,230,40),0,3)
        write(win, 'MinMax', (315,300),color=BLACK)
        pygame.draw.rect(win, colors[0][3], (300,370,230,40),0,3)
        write(win, 'AlphaBeta', (300,350),color=BLACK)
        pygame.draw.rect(win, colors[0][4], (300,420,230,40),0,3)
        write(win, 'DQN', (350,400),color=BLACK)

        write(win, 'Player 2',(750,150),color=BLACK)
        pygame.draw.rect(win, colors[1][0], (730,220,230,40),0,3)
        write(win, 'Human', (760,200),color=BLACK)
        pygame.draw.rect(win, colors[1][1], (730,270,230,40),0,3)
        write(win, 'Random', (750,250),color=BLACK)
        pygame.draw.rect(win, colors[1][2], (730,320,230,40),0,3)
        write(win, 'MinMax', (750,300),color=BLACK)
        pygame.draw.rect(win, colors[1][3], (730,370,230,40),0,3)
        write(win, 'AlphaBeta', (730,350),color=BLACK)
        pygame.draw.rect(win, colors[1][4], (730,420,230,40),0,3)
        write(win, 'DQN', (780,400),color=BLACK)

        
        pygame.draw.rect(win, 'gray', (530,470,200,45),0,3)
        write(win, 'Play', (575,448),color=BLACK)


        pygame.display.update()

    pygame.quit()

def write (surface, text, pos = (50, 20), color = BLACK, background_color = None):
    Font= pygame.font.SysFont("Segoe Print", 45)
    text_surface = Font.render(text, True, color, background_color)
    surface.blit(text_surface, pos)


if __name__ == '__main__':
    GUI()