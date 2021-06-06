class Settings():

    def __init__(self):
        self.screen_width=1100
        self.screen_height=600
        self.bg_color=(230, 230, 230)        
        self.ship_limit=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color= 60, 60, 60
        self.bullets_allowed=3
        self.fleet_drop_speed=10
        self.speed_up_scale=1.1
        self.score_scale=1.5
        
        self.initialize_dynamic_settings()
        self.aliens_points=50

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1 
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale

        self.aliens_points = int(self.aliens_points * self.score_scale)
        
        