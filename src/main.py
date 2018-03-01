from inout import Instance, Solution
from inout import get_ride_length, move_to
from solver import simulated_annealing
from operator import itemgetter


def reduce_to_undone_rides(rides):
    undone_rides = [ride for ride in rides if not ride.done]
    return undone_rides


def can_take_ride(current_time, pos_x, pos_y, ride):
    if ride.done:
        return False
    current_time, (pos_x, pos_y) = move_to(current_time, pos_x, pos_y, ride.a, ride.b)
    # Check that current time is after starting_time
    if current_time < ride.s:
        return False
    # Go to destination
    current_time, (pos_x, pos_y) = move_to(current_time, pos_x, pos_y, ride.x, ride.y)
    # Check that end time is before finish
    if current_time >= ride.f:
        return False

    return True


def take_ride(current_time, pos_x, pos_y, ride):
    current_time, (pos_x, pos_y) = move_to(current_time, pos_x, pos_y, ride.a, ride.b)
    current_time, (pos_x, pos_y) = move_to(current_time, pos_x, pos_y, ride.x, ride.y)

    return current_time, (pos_x, pos_y)


def assign_ride(current_time, pos_x, pos_y, rides):
    for ride in rides:
        if can_take_ride(current_time, pos_x, pos_y, ride):
            return ride

    return None


# def sort_rides_by_starting_date(rides):
#     return sorted(rides, key=itemgetter('s'))


def mark_ride_done(dataset, id):
    for i in range(len(dataset.rides)):
        if dataset.rides[i].id == id:
            dataset.rides[i].done = 1


def get_first_basic_solution(dataset):
    # dataset.rides = sort_rides_by_starting_date(dataset.rides)
    solution = {}
    for car_index in range(dataset.F):
        solution[car_index] = []
        pos_x, pos_y = 0, 0
        current_time = 0
        first_ride = assign_ride(current_time, pos_x, pos_y, dataset.rides)
        if first_ride is not None:
            current_time, (pos_x, pos_y) = take_ride(current_time, pos_x, pos_y, first_ride)
            ride = first_ride
            solution[car_index].append(ride)
            mark_ride_done(dataset, ride.id)
        while ride is not None:
            ride = assign_ride(current_time, pos_x, pos_y, dataset.rides)
            if ride is not None:
                current_time, (pos_x, pos_y) = take_ride(current_time, pos_x, pos_y, ride)
                solution[car_index].append(ride)
                mark_ride_done(dataset, ride.id)

    return solution

def output_solution(name):
    PATH_TO_DATA = '../data/' + name + ".in"
    OUTPUT_FILE = name + ".out"
    dataset = Instance(PATH_TO_DATA)
    trajets = get_first_basic_solution(dataset)
    solution = Solution(dataset)
    solution.trajets = trajets

    solution.write_solution(OUTPUT_FILE)


def output_all_solutions():
    names = ['a_example', 'b_should_be_easy', 'c_no_hurry', 'd_metropolis', 'e_high_bonus']
    for name in names:
        print('Doing ' + name)
        output_solution(name)


if __name__ == "__main__":
    output_all_solutions()
