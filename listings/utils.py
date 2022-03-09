from statistics import mean

def average(number_list: list, round_to: int) -> float:
    average_price = mean(number_list)
    return round(average_price, round_to)
