from inout import Instance, Solution
from solver import simulated_annealing

PATH_TO_DATA = "../data"

if __name__ == "__main__":
    dataset = Instance(PATH_TO_DATA)
    # Access the dataset variables by :
    # dataset.R, dataset.C, dataset.F, dataset.N, dataset.B, dataset.T, dataset.rides
    # dataset.rides is a dict with keys: id, a, b, x, y, s, f
