from source import board, player, ai
from pygame import locals
import pygame

class App:
    def __init__(self) -> None:
        self._running: bool = True
        self._display_surf: object = None
        self.weight: int = 640
        self.height: int = 400
        self.size: set[int] = (self.weight, self.height)

    def on_init(self) -> None:
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True 

    def on_event(self, event: object) -> None:
        if event.type == pygame.QUIT:
            self._running = False
            exit()
    
    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app: object = App()
    app.on_execute()


# TODO: initialze board
# TODO: fill board with numbers
# TODO: create launch window with play and visualize options
# TODO: implement player logic
# TODO: implement AI visualisation logic
