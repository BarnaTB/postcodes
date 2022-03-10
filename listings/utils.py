from geopy import distance
from statistics import mean

def average(number_list: list, round_to: int) -> float:
    """Helper function to compute the average of list of numbers

    Args:
        number_list[list]: A list of numbers whose average is to be computed
        round_to[int]: integer to which the average should be rounded
    """
    average_price = mean(number_list)
    return round(average_price, round_to)


def calculate_distance(first_coordinates: tuple, second_coordinates: tuple, round_to: int) -> dict:
    """Helper function to compute the distance between two points

    Args:
        first_coordinates[tuple]: Coordinates of point A
        second_coordinates[tuple]: Coordinates of point B
        round_to[int]: Number of decimal places to round the distance to
    """
    distance_in_km = distance.distance(
        first_coordinates, second_coordinates).km
    distance_in_miles = distance.distance(
        first_coordinates, second_coordinates).miles
    distance_between_coordinates = {
        "distance_in_km": f"{round(distance_in_km, round_to)}km",
        "distance_in_miles": f"{round(distance_in_miles, round_to)}miles",
    }
    return distance_between_coordinates
