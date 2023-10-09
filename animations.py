import math
from ursina import Entity, time

__time_stamp = 0.0
__original_positions = {}
__original_angel_z = {}
__original_angel_x = {}
__original_angel_y = {}

def animation_F(front_cubes, duration=1):
    frame_duration = duration * 30
    angle_rotation_per_frame = 90 / frame_duration
    global __time_stamp, __original_positions, __original_angel_z

    if __time_stamp > frame_duration:
        __reset()
        return True

    angle = float(angle_rotation_per_frame * __time_stamp)
    if __time_stamp <= frame_duration:
        for i, cube in enumerate(front_cubes):
            if isinstance(cube, Entity):
                if cube not in __original_positions:
                    __original_positions[cube] = cube.position
                    __original_angel_z[cube] = cube.rotation_z

                coord = __original_positions[cube]
                x = coord[0] * math.cos(math.radians(angle)) - coord[1] * math.sin(math.radians(angle))
                y = coord[0] * math.sin(math.radians(angle)) + coord[1] * math.cos(math.radians(angle))
                cube.position = (x, y, coord[2])
                cube.rotation_z = __original_angel_z[cube] + -angle

        if __time_stamp <= frame_duration:
            __time_stamp += 1

    return False


def __reset():
    global __time_stamp, __original_positions, __original_angel_x, __original_angel_y, __original_angel_z
    __time_stamp = 0
    __original_positions = {}
    __original_angel_x = {}
    __original_angel_y = {}
    __original_angel_z = {}
