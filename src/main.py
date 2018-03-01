from inout import Instance, Solution
from solver import simulated_annealing

PATH_TO_DATA = "../data"

if __name__ == "__main__":
    dataset = Instance(PATH_TO_DATA)
    print(dataset.R)
    print(dataset.C)
    print(dataset.F)
    print(dataset.N)
    print(dataset.B)
    print(dataset.T)
    print(dataset.rides)
    for ride in dataset.rides:
        print(ride.id, ' - ', ride.a, ride.b, ride.x, ride.y, ride.s, ride.f, ' - ', ride.done, ' - ', ride.length)

    # Access the dataset variables by :
    # dataset.R, dataset.C, dataset.F, dataset.N, dataset.B, dataset.T, dataset.rides
    # dataset.rides is a dict with keys: id, a, b, x, y, s, f
