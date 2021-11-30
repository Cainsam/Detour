import pygame
import city_events
import dictonaries
import io
from urllib.request import urlopen

import image_scraper
from city_events import car

# Initialize Pygame
pygame.init()
imageflag = 0

# Return a car image from the image scraper. If the image won't/can't be used, cycles through higher index choices.
def car_pic(index):
    try:
        image_url = image_scraper.get_imageAPI(index, car[0] + " " + car[1])
        image_str = urlopen(image_url).read()
        image_file = io.BytesIO(image_str)
        image = pygame.image.load(image_file)
        image = pygame.transform.scale(image, (500, 300))
    except:
       return car_pic(index + 1)
    return image

# Words/Dialogue rendering
title_font = pygame.font.Font('freesansbold.ttf', 64)
play_font = pygame.font.Font('freesansbold.ttf', 32)
dia_font = pygame.font.Font('freesansbold.ttf', 14)

# Different text options
def dialogue_text(dia, x, y, r, g, b):
    text = dia_font.render(dia, True, (r, g, b))
    screen.blit(text, (x, y))

def title_text(x,y):
    title = title_font.render("DETOUR", True, (255, 255, 255))
    screen.blit(title, (x, y))

def play_text(x,y, r, g, b):
    play = play_font.render("Play Game", True, (r, g, b))
    screen.blit(play, (x, y))

def exit_text(x,y, r, g, b):
    exit = play_font.render("Exit Game", True, (r, g, b))
    screen.blit(exit, (x, y))

# Place a sprite on the screen
def sprite_place(img,x,y):
    screen.blit(img, (x, y))

# Handles the many text screens in the game
def write(dia_options):
    for i in dia_options:
        if type(i) != str and type(i) != int:
            if i != []:
                dialogue_text(i[0], i[1], i[2], i[3], i[4], i[5])

# Create game screen
screen = pygame.display.set_mode((800, 600))

# Title/Icon
pygame.display.set_caption("Detour")
icon = pygame.image.load('PixelCar6.png')
pygame.display.set_icon(icon)

# Variable that controls what screen we are on
cur_screen = "Title Screen"

# City Map Sprite Images
city_red = pygame.image.load('city_red.png')
city_green = pygame.image.load('city_green.png')
city_grey = pygame.image.load('city_grey.png')
city_black = pygame.image.load('city_black.png')

# Game running loop. Everything under here is checked every frame.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background color
    screen.fill((30, 0, 15))

    # Title Screen-----

    # Background and Title Text
    if cur_screen == "Title Screen":
        background = pygame.image.load("TitleScreen.jpg")
        screen.blit(background, (-100, -100))
        title_text(255, 200)

        # Play Game Text
        if pygame.mouse.get_pos()[0] > 297 and pygame.mouse.get_pos()[0] < 472 and pygame.mouse.get_pos()[1] > 299 and pygame.mouse.get_pos()[1] < 329:
                play_text(300, 300, 255, 0, 0)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        cur_screen = "text"
        else:
            play_text(300, 300, 255, 255, 255)

        # Exit Game Text
        if pygame.mouse.get_pos()[0] > 302 and pygame.mouse.get_pos()[0] < 466 and pygame.mouse.get_pos()[1] > 354 and pygame.mouse.get_pos()[1] < 376:
            exit_text(302, 350, 255, 0, 0)
            if pygame.mouse.get_pressed()[0] == 1:
                running = False
        else:
            exit_text(302, 350, 255, 255, 255)
        pygame.display.update()

    # Map Screen-----
    if cur_screen == "map":
        background = pygame.image.load("map.jpg")
        screen.blit(background, (0, 0))

        # Automatically makes the current city red, and its connections green. All other cities greyed out.
        for city in dictonaries.city_arr:
            if city["Name"] == city_events.cur_city:
                sprite_place(city_red, city["x"], city["y"])
            elif city["Name"] in city_events.city_conn:
                if pygame.mouse.get_pos()[0] > city["x"] and pygame.mouse.get_pos()[0] < (city["x"] + 50) and pygame.mouse.get_pos()[1] > city["y"] and pygame.mouse.get_pos()[1] < (city["y"] + 50):
                    sprite_place(city_green, city["x"], city["y"])
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            city_events.cur_city = city["Name"] + " Start"
                            city_conn = city["Connections"]
                            cur_screen = "text"
                else:
                    sprite_place(city_grey, city["x"], city["y"])
            else:
                sprite_place(city_black, city["x"], city["y"])
        pygame.display.update()

        # Text Screen___
    if cur_screen == "text":
        background = pygame.image.load("blackscreen800.jpg")
        screen.blit(background, (0, 0))

        # Checking for special events like end of a city section or use of the image scraper
        if city_events.city_event(city_events.cur_city, 0)[9] == 1:
            city_events.cur_city = city_events.city_event(city_events.cur_city, 0)[5]
            cur_screen = "map"
        elif city_events.city_event(city_events.cur_city, 0)[9] == 2:
            if imageflag == 0:
                image = car_pic(0)
                imageflag = 1
            screen.blit(image, (150, 50))

        # Highlighting text when the mouse hovers over it
        if cur_screen == "text":
            if 420 > pygame.mouse.get_pos()[1] > 380:
                write(city_events.city_event(city_events.cur_city, 1))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        city_events.cur_city = city_events.city_event(city_events.cur_city, 0)[5]
            elif 470 > pygame.mouse.get_pos()[1] > 430:
                write(city_events.city_event(city_events.cur_city, 2))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        city_events.cur_city = city_events.city_event(city_events.cur_city, 0)[6]
            elif 520 > pygame.mouse.get_pos()[1] > 480:
                write(city_events.city_event(city_events.cur_city, 3))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        city_events.cur_city = city_events.city_event(city_events.cur_city, 0)[7]
            elif 570 > pygame.mouse.get_pos()[1] > 530:
                write(city_events.city_event(city_events.cur_city, 4))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        city_events.cur_city = city_events.city_event(city_events.cur_city, 0)[8]
            else:
                write(city_events.city_event(city_events.cur_city, 0))
            pygame.display.update()
