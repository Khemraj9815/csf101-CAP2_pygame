import pygame
import os

pygame.init()

#screen set up
screen_height = 1200
screen_width = 800
screen = pygame.display.set_mode((screen_height,screen_width))
bullets = []
bullets_velocity = 2
    

#size of the box
box_height = 100
box_width = 200
#position
gun_x = 550
gun_y = 700

input_rect = pygame.Rect(200, 200, 140, 32) 

#text = ''  # Initialize text variable

pygame.display.set_caption("math game")

#white = (255, 255, 255) #screen color
gun_image = pygame.image.load(os.path.join('Assets', 'tank.png'))

gun_height, gun_width = 80, 80
gun = pygame.transform.scale(gun_image, (gun_height,gun_width))


def drawing():
    screen.fill((255, 255, 255))
    screen.blit(gun, (550, 700))  #when you want to blit image into the screen
    

    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet)  # Draw the bullets as black rectangles
    pygame.display.update()

def handle_bullets(bullets):
    for bullet in bullets:
        bullet.y -= bullets_velocity  # Move the bullets upward 
        if bullet.y <= 0:
            bullets.remove(bullet)

def main():
    game_on = True
    while game_on:
        for event in pygame.event.get(): # every game event
            if event.type == pygame.QUIT:
                game_on = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    bullet = pygame.Rect(gun_x + gun_width/2, gun_y, 5, 10)
                    bullets.append(bullet)
               

        handle_bullets(bullets) #moves the bullets position

        drawing()
    pygame.quit()

if __name__ == "__main__":
    main()