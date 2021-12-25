class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Bullets
        self.bullet_speed_factor = 10
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = 60,60,60
        self.bullets_allowed = 20

        #Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1