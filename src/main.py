from inout import Instance, Solution
from inout import get_ride_length, move_to
from solver import simulated_annealing

PATH_TO_DATA = "../data/c_no_hurry.in"

def reduce_to_undone_rides(rides):
    undone_rides = [ride for ride in rides if not ride.done]
    return undone_rides

def can_take_ride(current_time, pos_x, pos_y, ride):
    if ride.done:
        return False
    current_time, (pos_x, pos_y) = move_to(current_time, ride.a, ride.b)
    # Check that current time is after starting_time
    if current_time < ride.s:
        return False
    # Go to destination
    current_time, (pos_x, pos_y) = move_to(current_time, ride.x, ride.y)
    # Check that end time is before finish
    if current_time >= ride.f:
        return False

    return True

def assign_ride(current_time, pos_x, pos_y, rides):
    for ride in rides:
        if can_take_ride(current_time, pos_x, pos_y, ride):
            return ride

    return None


if __name__ == "__main__":
    dataset = Instance(PATH_TO_DATA)
    print(len(dataset.rides))
    for car_index in dataset.F:
        pos_x, pos_y = 0
        current_time = 0

    # print(dataset.R)
    # print(dataset.C)
    # print(dataset.F)
    # print(dataset.N)
    # print(dataset.B)
    # print(dataset.T)
    # print(dataset.rides)
    # for ride in dataset.rides:
    #     print(ride.id, ' - ', ride.a, ride.b, ride.x, ride.y, ride.s, ride.f, ' - ', ride.done, ' - ', ride.length)

    # Access the dataset variables by :
    # dataset.R, dataset.C, dataset.F, dataset.N, dataset.B, dataset.T, dataset.rides
    # dataset.rides is a dict with keys: id, a, b, x, y, s, f
