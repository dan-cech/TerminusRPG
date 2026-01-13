import pygame as pg

pg.mixer.init()

def play_music(file):
    pg.mixer.music.load(file)
    pg.mixer.music.play(-1)   # -1 = loop

def play_sound(file):
    pg.mixer.music.load(file)
    pg.mixer.music.play(1)

def stop_music():
    pg.mixer.music.stop()