import unittest
import pygame
from main import Button, handle_bullets, movement_of_player, on_screen

class TestGame(unittest.TestCase):

    def test_button_click(self):
        # Test click detection
        button = Button(100, 200, pygame.Surface((50, 50))) 
        button.draw()
        self.assertFalse(button.click)
        
        # Simulate mouse click
        button.rect.collidepoint((120, 220)) 
        pygame.mouse.get_pressed.return_value = [1, 0, 0]
        button.draw()        
        self.assertTrue(button.click)

        # Test reset click
        pygame.mouse.get_pressed.return_value = [0, 0, 0]
        button.draw()
        self.assertFalse(button.click)

    def test_player_movement(self):
        # Test player movement
        movement_of_player()
        self.assertEqual(right_player_y, 550) 
        self.assertEqual(left_player_y, 200)

        # Simulate keypresses
        pygame.key.get_pressed.return_value = [1, 0, 0, 0] # Up key
        movement_of_player()
        self.assertLess(right_player_y, 550)

        pygame.key.get_pressed.return_value = [0, 0, 1, 0] # Down key
        movement_of_player()        
        self.assertGreater(right_player_y, 550)

        pygame.key.get_pressed.return_value = [0, 1, 0, 0] # W key
        movement_of_player()
        self.assertLess(left_player_y, 200)

        pygame.key.get_pressed.return_value = [0, 0, 0, 1] # S key
        movement_of_player()        
        self.assertGreater(left_player_y, 200)

    def test_bullet_handling(self):
        # Test bullet collision
        right_bullets = [pygame.Rect(100, 100, 10, 5)]
        left_bullets = []
        
        handle_bullets(right_bullets, left_bullets, None, None)
        self.assertEqual(len(right_bullets), 1)

        left_player_rect.x = 90
        handle_bullets(right_bullets, left_bullets, None, left_player_rect)
        self.assertEqual(len(right_bullets), 0)

        # Test bullet removal off screen
        right_bullets = [pygame.Rect(-10, 100, 10, 5)]
        handle_bullets(right_bullets, left_bullets, None, None)
        self.assertEqual(len(right_bullets), 0)

    def test_on_screen(self):
        # Mock screen surface
        screen = pygame.Surface((1200, 800))
        
        # Test on_screen renders correctly
        on_screen(10, 10)
        self.assertNotEqual(screen.get_at((0, 0)), (255, 255, 255))

        right_text = screen.get_at((1180, 10))
        self.assertEqual(right_text, (0, 0, 0))

        left_text = screen.get_at((20, 10))
        self.assertEqual(left_text, (0, 0, 0))
        
if __name__ == '__main__':
    unittest.main()
