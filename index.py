import pygame
import pytmx
from pytmx.util_pygame import load_pygame

from main import player_pos_x, screen, player_pos_y


class Game:

    def __init__(self):


        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280,720))

        self.font = pygame.font.Font('/Users/harshmishra/PycharmProjects/PACMAN/font/Pixeltype.ttf', 32)
        self.player_pos_x = self.screen.get_width()/2
        self.player_pos_y = self.screen.get_height()/2

        self.dt = 0
        self.text =  self.font.render(f"{self.coordinates}", True, "blue")
        self.textRect = self.text.get_rect(center=(400, 250))
        self.screen.blit(self.text, self.textRect)
        self.coordinates = (self.player_pos_x,self.player_pos_y)
        self.tmx_data = load_pygame('/Users/harshmishra/PycharmProjects/PACMAN/map/pacMap.tmx')

    def render_map(self):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y , gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        self.screen.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

    def ball_movement(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.player_pos_y -= 300 * self.dt
        if keys[pygame.K_a]:
            self.player_pos_x -= 300 * self.dt
        if keys[pygame.K_s]:
            self.player_pos_y += 300 * self.dt
        if keys[pygame.K_d]:
            self.player_pos_x += 300 * self.dt

    def ball_out(self):

        if self.player_pos_y > 790:
            self.player_pos_y = 0
        elif self.player_pos_y < -10:
            self.player_pos_y = 780
        if self.player_pos_x > 1290:
           self.player_pos_x = 0
        elif self.player_pos_x < -10:
            self.player_pos_x = 1290

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.fill("black")
            self.render_map()
            self.ball_movement()
            self.ball_out()
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()
