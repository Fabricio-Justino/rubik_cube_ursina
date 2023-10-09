from ursina import *
from cube import Cube
from animations import *
from cube_filter import *

animations_end = False
can_animate = False
times_tamp = 0


def update():
    global times_tamp
    global animations_end
    global can_animate

    times_tamp += 1

    if held_keys['w'] and not can_animate:
        can_animate = True

    if not animations_end and can_animate:
        animations_end = animation_F(front_cubes)
    else:
        can_animate = False
        animations_end = False
def init_cubes():
    cubes_layers = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                cube = Cube()
                cube.position = (1 * x, 1 * y, 1 * z)
                cubes_layers.append(cube)
    return cubes_layers


app = Ursina(borderless=False, fullscreen=True)
EditorCamera()

cubes = init_cubes()

front_cubes = get_F_layer(cubes)



app.run()
