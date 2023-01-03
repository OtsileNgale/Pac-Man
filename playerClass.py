import pygame
from Settings import *

vector = pygame.math.Vector2

class Player:
    def __init__(self, app, pos):
        self.app = app
        self.start_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vector(1,0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 0
        self.lives = 3
        
    def update(self):
        if self.able_to_move:
          self.pix_pos += self.direction * self.speed
        if self.time_to_move:
          if self.stored_direction != None:
              self.direction = self.stored_direction
          self.able_to_move = self.can_move

#Set grid position in reference to pixel position

        self.grid_pos[0] = (self.grid_pos[0] - TOP_BOTTOM_BUFFER + self.app.cell_width//2)//self.app.cell_width +1
        self.grid_pos[1] = (self.grid_pos[1] - TOP_BOTTOM_BUFFER + self.app.cell_height//2)//self.app.cell_height +1
        if self.on_token:
            self.eat_token
            
    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x),
                                                            int(self.pix_pos.y)), self.app.cell_width//2-2)

#Drawing player lives
        for x in range(player.lives):
            pygame.draw.circle(self.app.screen, PLAYER_COLOUR, 3(0 + 20*X, HEIGHT - 15), 7)

#Drawing the grid pos rectangle
        pygame.draw.rect(self.app.screen, RED, (self.grid_pos[0]*self.app.cell_width+TOP_BOTTOM_BUFFER//2, self.grid_pos[1]*self.app.cell_height+TOP_BOTTOM_BUFFER//2, self.app.cell_width, self.app.cell_height), 1)
        
    def on_token(self):
        if self.grid_pos in self.app.tokens:
            if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
                if self.direction == vector(1, 0) or self.direction == vec(-1, 0):
                    return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.direction == vector(0, 1) or self.direction == vector(0, -1):
                return True
        return False
    
    def eat_token(self):
        self.app.tokens.remove(self.grid_pos)
        self.current += 1
        
    def move(self, direction):
        self.stored_direction = direction
        
    def get_pix_pos(self):
        return vector((self.grid_pos[0]*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2,
                   (self.grid_pos[1]*self.app.cell_height) +
                   TOP_BOTTOM_BUFFER//2+self.app.cell_height//2)

        print(self.grid_pos, self.pix_pos)

    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True