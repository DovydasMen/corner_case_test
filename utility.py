from typing import Union, List, Dict


def get_illumination_intencity(x: int) -> Union[int, float]:
    """returning  intensity of illuminations, where x distance from street light"""
    return 3 ** (-((x / 100) ** 2))


def get_list_of_all_bulbs(road_lenght: int) -> List[int]:
    """After recieving road lenght(It's freezed gap every 20m),
    returning list of bulbs starting from index 0 at the biggining.)"""
    return list(range(int((road_lenght / 20) + 1)))


def set_values_of_ignored_illuminations(
    illumination_index: Dict[str, float]
) -> Dict[str, float]:
    """We are expecting to get dictionary with illumination index
    and return dictionary with 0 values for those who's intensity is <0.01"""
    for key in list(illumination_index.keys()):
        if illumination_index[key] < 0.01:
            illumination_index[key] = 0
    return illumination_index


def intensity_of_light(first_light_bulb: int, secound_light_bulb: int) -> float:
    """Return float value of illumination"""
    road_range = (first_light_bulb - secound_light_bulb) * 20
    return get_illumination_intencity(road_range)
