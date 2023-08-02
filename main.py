from typing import Union, List, Dict


def get_illumination_intencity(x: int) -> Union[int, float]:
    """returning  intensity of illuminations, where x distance from street light"""
    return 3 ** (-((x / 100) ** 2))


def get_list_of_all_bulbs(road_lenght: int) -> List[int]:
    """After recieving road lenght(It's freezed gap every 20m),
    returning list of bulbs starting from index 0 at the biggining.)"""
    return list(range(int((road_lenght / 20) + 1)))


def set_value_of_ignored_illuminations(
    illumination_index: Dict[str, float]
) -> Dict[str, float]:
    for key in list(illumination_index.keys()):
        if illumination_index[key] < 0.01:
            illumination_index[key] = 0
    return illumination_index


def find_index_of_the_darkest_street_light(
    road_lenght: int, not_working_street_lighs: List[int]
) -> int:
    illumination_index: Dict[str, float] = {}
    all_lights: List[int] = sorted(get_list_of_all_bulbs(road_lenght=road_lenght))
    not_working_lighs: List[int] = sorted(not_working_street_lighs)
    # code bellow needs to be reviewed. I think it's too complicated.
    for light in all_lights:
        if light not in not_working_lighs:
            continue
        else:
            gaps_between_lights: Dict[str, float] = {}
            for iterating_light in range(len(all_lights)):
                if iterating_light in not_working_lighs or iterating_light == light:
                    continue
                else:
                    gaps: int = light - iterating_light
                    road_range: int = gaps * 20
                    intencity: float = get_illumination_intencity(road_range)
                    gaps_between_lights[f"{iterating_light} - {light}"] = intencity
        illumination_index[light] = max(gaps_between_lights.values())

    # part bellow, would need to have function.
    for key in list(illumination_index.keys()):
        if illumination_index[key] < 0.01:
            illumination_index[key] = 0
    return min(illumination_index, key=illumination_index.get)


if __name__ == "__main__":
    print(find_index_of_the_darkest_street_light(200, [4, 5, 6]))
