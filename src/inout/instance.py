from .ride import Ride


class Instance:
    def __init__(self, fpath, name='instance'):
        self.fpath = fpath
        self.read_dataset()
        self.name = name

    def read_dataset(self):
        with open(self.fpath, 'r') as dataset_file:

            self.R, self.C, self.F, self.N, self.B, self.T = [int(i) for i in dataset_file.readline().split(' ')]
            self.rides = []
            for i in range(self.N):
                a, b, x, y, s, f = [int(i) for i in dataset_file.readline().split(' ')]
                self.rides.append(Ride(i, a, b, x, y, s, f))


if __name__ == "__main__":
    file_path = "../../data/c_no_hurry.in"
    dataset = Instance(file_path)
    print(dataset.R)
    print(dataset.C)
    print(dataset.F)
    print(dataset.N)
    print(dataset.B)
    print(dataset.T)
    print(dataset.rides)
    for ride in dataset.rides:
        print(ride.id, ' - ', ride.a, ride.b, ride.x, ride.y, ride.s, ride.f, ' - ', ride.done, ' - ', ride.length)
