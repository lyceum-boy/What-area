import sys

from data.geocoder import get_coordinates, get_nearest_object

toponym_to_find = " ".join(sys.argv[1:])

if toponym_to_find:
    point = get_coordinates(toponym_to_find)
    # Получаем район.
    district_name = get_nearest_object(point, "district")
    print(district_name)
