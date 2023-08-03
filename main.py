from typing import Union, List, Dict
from utility import (
    get_list_of_all_bulbs,
    set_values_of_ignored_illuminations,
    intensity_of_light,
)


def find_index_of_the_darkest_street_light(
    road_lenght: int, not_working_street_lighs: List[int]
) -> int:
    try:
        illumination_index: Dict[str, float] = {}
        all_lights: List[int] = sorted(get_list_of_all_bulbs(road_lenght=road_lenght))
        not_working_lighs: List[int] = sorted(not_working_street_lighs)
        for light in not_working_lighs:
            gaps_between_lights_with_illuminatio_indexes: Dict[str, float] = {}
            for iterating_light in range(len(all_lights)):
                if iterating_light in not_working_lighs or iterating_light == light:
                    continue
                else:
                    intencity: float = intensity_of_light(light, iterating_light)
                    gaps_between_lights_with_illuminatio_indexes[
                        f"{iterating_light} - {light}"
                    ] = intencity
            illumination_index[light] = max(
                gaps_between_lights_with_illuminatio_indexes.values()
            )
        illumination_index_with_correct_values = set_values_of_ignored_illuminations(
            illumination_index
        )
        return min(illumination_index_with_correct_values, key=illumination_index.get)
    except TypeError:
        print("Please define correct type values!")
    except Exception as e:
        print(f"We occured unexpected error: ", str(e))


if __name__ == "__main__":
    print(find_index_of_the_darkest_street_light(200, [4, 5, 6]))
