import pygame.image
from pygame import Rect, Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_TITLE, MENU_OPTION, MENU_COMANDS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/universeBG.png')
        self.rect = self.surf.get_rect(left=0, top =0)

    def run(self, ):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=130, text='Pixel Invaders', text_color=COLOR_TITLE, text_center_pos =((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=60, text=MENU_OPTION[i], text_color=COLOR_TITLE, text_center_pos =((WIN_WIDTH / 2), 400 + 70 * i))
                self.menu_text(text_size=60, text=MENU_COMANDS[i], text_color=COLOR_TITLE, text_center_pos=((WIN_WIDTH / 2), 700 + 70 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Segoe UI Symbol", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)