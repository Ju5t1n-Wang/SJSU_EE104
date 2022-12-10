#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 19:34:06 2022

@author: justinwang
"""

import pgzrun #runs the pygame 
from pgzero.builtins import *
import pygame
from random import randint
from pgzero.builtins import Actor #object in the game (like sprites in scratch)


WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

move_list = []
display_list = []

score1 = 0
score2 = 0
current_move = 0
count = 5
dance_length = 5
display_player = True
display_time = 3

player1 = True
player2 = False
say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor("dancer-start")
dancer.pos = CENTER_X + 5, CENTER_Y - 40

up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

def draw():
    global game_over, score1, score2, say_dance
    global count, show_countdown, display_player
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Player 1 score: " +
                         str(score1), color="black",
                         topleft=(10, 10))
        screen.draw.text("Player 2 score: " +
                         str(score2), color="black",
                         topleft=(650, 10))
        if display_player:
            if player1:
                screen.draw.text("Player 1 you're up!", 
                                 color="black",
                                 topleft=(CENTER_X - 180, 150), fontsize=60)
            if player2:
                screen.draw.text("Player 2 you're up!", 
                                 color="black",
                                 topleft=(CENTER_X - 180, 150), fontsize=60)
        else:
            if say_dance:
                screen.draw.text("Dance!", color="black",
                                 topleft=(CENTER_X - 65, 150), fontsize=60)
            if show_countdown:
                screen.draw.text(str(count), color="black",
                                     topleft=(CENTER_X - 8, 150), fontsize=60)
    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Player 1 score: " +
                         str(score1), color="black",
                         topleft=(10, 10))
        screen.draw.text("Player 2 score: " +
                         str(score2), color="black",
                         topleft=(650, 10))
        screen.draw.text("GAME OVER!", color="black",
                         topleft=(CENTER_X - 130, 150), fontsize=60)
        screen.draw.text("Song: Falling Sky", color="blue",
                         topleft=(CENTER_X - 130, 200), fontsize=60)
        screen.draw.text("By: audionautix", color="blue",
                         topleft=(CENTER_X - 130, 250), fontsize=60)
    return

def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"
    return

def update_dancer(move):
    global game_over
    if not game_over:
        if move == 0:
            up.image = "up-lit"
            dancer.image = "dancer-up"
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer, 0.5)
        else:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer, 0.5)
    return

def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves, 1)
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True
        show_countdown = False
    return

def generate_moves():
    global move_list, dance_length, count
    global show_countdown, say_dance
    count = 5
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        rand_move = randint(0, 3)
        move_list.append(rand_move)
        display_list.append(rand_move)
    show_countdown = True
    countdown()
    return

def countdown():
    global count, game_over, show_countdown
    if count > 1:
        count = count - 1
        clock.schedule(countdown, 1)
    else:
        show_countdown = False
        display_moves()
    return

def next_move():
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move = current_move + 1
    else:
        moves_complete = True
    return

def on_key_up(key):
    global score1, score2, game_over, move_list, current_move, player1, player2, display_time, say_dance
    print(key)
    if player1:
        if key == keys.UP:
            update_dancer(0)
            if move_list[current_move] == 0:
                score1 = score1 + 1
                next_move()
            else:
                player1 = False
                player2 = True
                say_dance = False
                display_time = 3
                start_game()
        elif key == keys.RIGHT:
            update_dancer(1)
            if move_list[current_move] == 1:
                score1 = score1 + 1
                next_move()
            else:
                player1 = False
                player2 = True
                say_dance = False
                display_time = 3
                start_game()
        elif key == keys.DOWN:
            update_dancer(2)
            if move_list[current_move] == 2:
                score1 = score1 + 1
                next_move()
            else:
                player1 = False
                player2 = True
                say_dance = False
                display_time = 3
                start_game()
        elif key == keys.LEFT:
            update_dancer(3)
            if move_list[current_move] == 3:
                score1 = score1 + 1
                next_move()
            else:
                player1 = False
                player2 = True
                say_dance = False
                display_time = 3
                start_game()
    if player2:
            if key == keys.W:
                update_dancer(0)
                if move_list[current_move] == 0:
                    score2 = score2 + 1
                    next_move()
                else:
                    game_over = True
            elif key == keys.D:
                update_dancer(1)
                if move_list[current_move] == 1:
                    score2 = score2 + 1
                    next_move()
                else:
                    game_over = True
            elif key == keys.S:
                update_dancer(2)
                if move_list[current_move] == 2:
                    score2 = score2 + 1
                    next_move()
                else:
                    game_over = True
            elif key == keys.A:
                update_dancer(3)
                if move_list[current_move] == 3:
                    score2 = score2 + 1
                    next_move()
                else:
                    game_over = True
    return

def update():
    global game_over, current_move, moves_complete
    if not game_over:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
    else:
        music.stop()
        
def start_game():
    global player1, player2, display_player, display_time
    if display_time > 1:
        display_player = True
        display_time = display_time - 1
        clock.schedule(start_game, 1)
    else:
        display_player = False
        generate_moves() 
        pygame.mixer.init()
        music.play("falling-sky")    

start_game()
pgzrun.go()