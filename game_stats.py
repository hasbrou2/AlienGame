class GameStats():
    """Track Game Statistics"""

    def __init__(self, ai_settings):
        """Initialize Statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #High Score should never be reset
        self.high_score = 0

        #Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize Statistics that can change during the game"""
        self.ships_left  = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    

    

        