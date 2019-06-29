import math
from src.locations import dict_location


def get_distance(input_x: int, input_y: int, input_z: int, location: dict):
    """
    Calculates distance based on inputs.
    :param input_x:
    :param input_y:
    :param input_z:
    :param location:
    :return:
    """
    a = math.sqrt(
        math.pow(input_x - location['x'], 2) + math.pow(input_y - location['y'], 2) + math.pow(input_z - location['z'],
                                                                                               2)

    )
    return a


print(get_distance(36, 125, -587, dict_location['location_a']))
