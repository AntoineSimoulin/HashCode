def get_ride_length(a, b, x, y):
    return abs(x-a) + abs(y - b)


def move_to(current_time, a, b):
    current_time += get_ride_length(a, b)
    return current_time, (a, b)
