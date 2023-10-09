from ursina import *


class Cube(Entity):

    def __init__(self):
        super().__init__()
        self.model = 'custom_cube.obj'
        self.texture = 'rubik_texture.png'
        self.scale = (1, 1, 1)
        self.rotation_z = 0
    def update(self):
        pass
