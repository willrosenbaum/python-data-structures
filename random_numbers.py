import random

# seed the random number generator
random.seed(1)

# write a method that generates a list of a specified length containting random numbers in a specified range. The range is a tuple of two real numbers.

def generate_random_numbers(length: int, bounds: tuple[float, float]) -> list[float]:
    return [random.uniform(bounds[0], bounds[1]) for _ in range(length)]

# print a a given list of floating point numbers rounded to two decimal places separated by commas
def print_floats(numbers: list[float]) -> None:
    for number in numbers:
        print(f"{number:.2f}", end=", " if number != numbers[-1] else "\n")

# given a list of x values and a list of y values, find the pair with the smallest distance and return the pair of indices corresponding to those points
def find_closest_points(x_vals: list[float], y_vals: list[float]) -> tuple[int, int]:
    min_dist = float('inf')
    min_pair = (0, 0)
    for i in range(len(x_vals)):
        for j in range(i):
            dist = (x_vals[i] - x_vals[j]) ** 2 + (y_vals[i] - y_vals[j]) ** 2
            if dist < min_dist:
                min_dist = dist
                min_pair = (i, j)
    return min_pair

x_vals = sorted(generate_random_numbers(20, (0, 10)))       
y_vals = generate_random_numbers(20, (0, 5))

# find the closest pair of points
print('closest pair of points: ', find_closest_points(x_vals, y_vals))
print('closest pair of points on left half: ', find_closest_points(x_vals[:10], y_vals[:10]))
print('closest pair of points on right half: ', find_closest_points(x_vals[10:], y_vals[10:]))

print_floats(x_vals)
print_floats(y_vals)