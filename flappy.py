import pygame
import random

window_width = 600
window_height = 499

window = pygame.display.set_mode((window_height, window_width))
elevation = window_height * 0.9
images = {}
framePerSecond = 32
bird_image = "images/bird.png"
background_image = "images/background.png"
tree_image = "images/tree.png"

if __name__ == "__main__":
    # initilize the frame
    pygame.init()
    framePerSecond_clock = pygame.time.Clock()

    pygame.display.set_caption("the new flappy game")

    images['birdImage'] =pygame.image.load(bird_image).convert_alpha()
    images['backgroundImg'] = pygame.image.load(background_image).convert_alpha()
    images['tree'] = pygame.image.load(tree_image).convert_alpha()

    print("Welcome to the Game")
    print("press enter button to start the game")

while True:

    bird_horizontal =int(window_width/5)
    bird_vertical = int(window_height-images['birdImage'].get_height()/2)


