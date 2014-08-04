import pygame
from pygame.locals import *
import pygame.mixer
import serial
import time

#portStr = '\dev\ttyACM0'
#arduino = serial.Serial('/dev/ttyACM0', 9600)

pygame.display.set_mode((120, 120), DOUBLEBUF | HWSURFACE)
pygame.init()

pygame.mixer.init()

snare = pygame.mixer.Sound('snare.wav')
crash = pygame.mixer.Sound('crash.wav')
kick = pygame.mixer.Sound('kick.wav')

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snare.play()
                #print 'a'
            elif event.key == pygame.K_RIGHT:
                crash.play()
                #print 'b'
            elif event.key == pygame.K_UP:
                kick.play()
                #print 'c'


