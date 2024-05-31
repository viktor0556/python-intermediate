import pygame as pg
import moderngl as mgl
import sys

class Graphicsengine:
    def __init__(self, win_size=(1600, 900)):
        pg.init()

        self.WIN_SIZE = win_size

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_get_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_get_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        self.ctx = mgl.create_context()

        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def render(self):
        