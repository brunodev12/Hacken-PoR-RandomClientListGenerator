import random
import math
from data.constants import ranges_dict, probabilities_dict
from decimal import Decimal, ROUND_DOWN


def get_decimal_length(number):
    string = "{:.20f}".format(number).rstrip('0')
    if '.' in string:
        decimals = string.split('.')[1].rstrip('0')
        decimal_length = len(decimals)
        return decimal_length
    else:
        return 0


def generate_number_with_decimals(range_:list, decimals:int) -> str:

    adjusted_number = Decimal(random.uniform(range_[0], range_[1]))

    factor = Decimal('1.' + '0' * decimals)
    adjusted_number = adjusted_number.quantize(factor, rounding=ROUND_DOWN)

    if adjusted_number == 0:
        formatted_number = "0.0"
    else:
        formatted_number = f"{adjusted_number:f}"

    return formatted_number


def generate_number(minimum, maximum, displacement=3, currency=None):
    
    decimals = get_decimal_length(minimum)

    ranges = ranges_dict.get(currency, None)
    probabilities = probabilities_dict.get(currency, None)
    if ranges is None:
        divisions = int(math.log10(maximum / minimum))
        scale_factor = math.log10(maximum / minimum) / divisions
        ranges = []
        probabilities = []
        total_sum = 0
        for i in range(divisions):
            lower_limit = minimum * 10**(i * scale_factor)
            upper_limit = minimum * 10**((i + 1) * scale_factor)
            range_ = (lower_limit, upper_limit)
            ranges.append(range_)
            if i < divisions // displacement:
                probability = (i + 1) / (divisions // displacement + 1)
            else:
                probability = (divisions - i) / ((displacement-1) * divisions // displacement)
            probabilities.append(probability)
            total_sum += probability
        probabilities = [p / total_sum for p in probabilities]

    random_number = round(random.random(), decimals)

    cumulative_probability = 0
    for range_, probability in zip(ranges, probabilities):
        cumulative_probability += probability
        if random_number < cumulative_probability:
            adjusted_number = generate_number_with_decimals(range_, decimals)
            return adjusted_number

    adjusted_number = generate_number_with_decimals(range_, decimals)
    return adjusted_number