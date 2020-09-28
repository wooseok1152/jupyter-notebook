import pygame
import time

music_file = ".\\기억을 걷는 시간.mp3"

pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

max_time_end = time.time() + (60 * 10)
while True:

    if time.time() > max_time_end:

        break
