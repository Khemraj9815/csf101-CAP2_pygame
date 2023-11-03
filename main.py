import pygame
pygame.init()

import os

# Screen setup
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("war game") 
white = (255,255,255)

info_font = pygame.font.SysFont("comicsans", 40)
button_info = pygame.font.SysFont("comicsans", 30)
play_img = pygame.image.load("/home/khemrajghalley/Desktop/khem/pygame/Assets/play.jpg").convert_alpha()
exit_img = pygame.image.load("/home/khemrajghalley/Desktop/khem/pygame/Assets/exit.jpg").convert_alpha()
play_height, play_width = 255,155
exit_height, exit_width = 250,150

play = pygame.transform.scale(play_img, (play_height, play_width))
exit = pygame.transform.scale(exit_img, (exit_height, exit_width))

class Button():
    def __init__(self,x,y,image):
        self.image =  image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.click = False

    def draw(self):
        action = False
        #get mouse position 
        position = pygame.mouse.get_pos()

        left_info = info_font.render("left player button", 1, black)
        screen.blit(left_info,(150,80))
        left_up = button_info.render("up button: W", 1,black)
        screen.blit(left_up,(150,140))
        left_down = button_info.render("down button: S",1,black)
        screen.blit(left_down,(150,180))
        fire = button_info.render("fire: alt",1,black)
        screen.blit(fire, (150,220))

        right_info = info_font.render("right player button", 1, black)
        screen.blit(right_info,(650,80))
        right_up = button_info.render("up button: up", 1,black)
        screen.blit(right_up,(650,140))
        right_down = button_info.render("down button: down",1,black)
        screen.blit(right_down,(650,180))
        fire1 = button_info.render("fire: alt",1,black)
        screen.blit(fire1, (650,220))
        #check mouse position and click condition
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                action = True

        # Reset the click state if mouse is not pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

play_button  = Button(350, 350, play)
exit_button  = Button(600,350, exit)

left_player_height, left_player_width = 70, 70
left_player = pygame.image.load(os.path.join('Assets', 'left.jpg'))
left = pygame.transform.scale(left_player, (left_player_height, left_player_width))

right_player_height, right_player_width = 70, 70
right_player = pygame.image.load(os.path.join('Assets', 'right.jpg'))
right = pygame.transform.scale(right_player, (right_player_height, right_player_width))

right_player_x, right_player_y = 1000, 550  # Initial position of the right player
left_player_x, left_player_y = 100, 200  # Initial position of the left player

velocity_of_right_player = 0.7
velocity_of_left_player = 0.7

health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('comicsans', 100)
black = (0,0,0)
right_player_health = 10
left_player_health = 10
gun_fire_sound = pygame.mixer.Sound((os.path.join("Assets", "gun_sound.mp3")))

def on_screen(right_player_health,left_player_health):
    screen.fill((255, 255, 255))
    right_player_health_text = health_font.render("Health:" + str(right_player_health), 1, black)
    left_player_health_text = health_font.render("Health:" + str(left_player_health), 1, black)
    screen.blit(right_player_health_text, (screen_width-220,10))
    screen.blit(left_player_health_text, (20,10))

    screen.blit(left, (left_player_x, left_player_y))
    screen.blit(right, (right_player_x, right_player_y))

    for bullet in right_player_bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet)

    
    for bullet in left_player_bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet)

    pygame.display.update()

def movement_of_player():
    global right_player_y  
    global left_player_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and right_player_y + velocity_of_right_player > 0:
        right_player_y -= velocity_of_right_player
    if keys[pygame.K_DOWN] and right_player_y + right_player_height < screen_height:
        right_player_y += velocity_of_right_player
    if keys[pygame.K_w] and left_player_y + velocity_of_left_player > 0:
        left_player_y -= velocity_of_left_player
    if keys[pygame.K_s] and left_player_y + left_player_height < screen_height:
        left_player_y += velocity_of_left_player
    right_player_rect.y = right_player_y
    left_player_rect.y = left_player_y

right_player_bullets_velocity = 2
left_player_bullets_velocity = 2
right_player_bullets = []
left_player_bullets = []

right_hit = pygame.USEREVENT + 1
left_hit = pygame.USEREVENT + 2

right_player_rect = pygame.Rect(right_player_x, right_player_y, right_player_width, right_player_height)
left_player_rect = pygame.Rect(left_player_x, left_player_y, left_player_width, left_player_height)


def handle_bullets(right_player_bullets, left_player_bullets,right_player,left_player):
    for bullet in right_player_bullets:
        bullet.x -= right_player_bullets_velocity
        if left_player_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(left_hit))
            right_player_bullets.remove(bullet)
        elif bullet.x > screen_width:                                                                                                                                                                                                                                 
            right_player_bullets.remove(bullet)
    for bullet in left_player_bullets:
        bullet.x += left_player_bullets_velocity
        if right_player_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(right_hit))
            left_player_bullets.remove(bullet)
        elif bullet.x < 0:
            left_player_bullets.remove(bullet)

def re_setup():
    global left_player_health, right_player_health , right_player_x,left_player_x,right_player_y,left_player_y
    left_player_health = 10
    right_player_health = 10
    left_player_x = 100
    left_player_y = 200
    right_player_x = 1000
    right_player_y = 550

def result(text):
    draw_text = winner_font.render(text,1,black)
    screen.blit(draw_text, (screen_width/2 - draw_text.get_width()/2, screen_height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    re_setup()  # restart the game
    main()

def main():
    global left_player_health, right_player_health                         
    game_on = True
    winner = None
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RALT:
                    bullet = pygame.Rect(right_player_x + right_player_width // 2 - 25, right_player_y + right_player_height // 2-20, 10, 5)
                    right_player_bullets.append(bullet)
                    gun_fire_sound.play()
                
                if event.key == pygame.K_LALT:
                    bullet = pygame.Rect(left_player_x + left_player_width // 2+25, left_player_y + left_player_height//2-20,10,5)
                    left_player_bullets.append(bullet)
                    gun_fire_sound.play()

            if event.type == right_hit:
                right_player_health -= 1

            if event.type == left_hit:
               left_player_health -= 1
               
            winner = ""
            if right_player_health <= 0:
                winner = "left player wins"
                result(winner)

            if left_player_health <= 0:
                winner = "right player wins"
                result(winner)
        movement_of_player()
        handle_bullets(right_player_bullets,left_player_bullets,right_player,left_player)
        on_screen(right_player_health,left_player_health)
        pygame.display.update()
    pygame.quit()
 
game_on = True
while game_on:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    if play_button.draw() == True:
        main()
    
    if exit_button.draw() == True:
        pygame.quit()

    pygame.display.update()
pygame.quit()
