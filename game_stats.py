class GameStats():
    """Track Game Statistics"""

    def __inti__(self, ai_settings):
        """Initialize Statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize Statistics that can change during the game"""
        self.ships_left  = self.ai_settings.ship_limit

        