import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():

    #Initialize game, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create and instance to store game statistics. 
    stats = GameStats(ai_settings)


    # Set the background color.
    bg_color = (230, 230, 230)

    #Make Ship, group of bullets, and a group of aliens
    ship = Ship(ai_settings,screen)
    aliens = Group()
    bullets = Group()

    #Creating the fleet of aliens.
    gf.create_fleet(ai_settings, screen,ship ,aliens)


    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update() 
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship ,aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens ,bullets)
run_game()    