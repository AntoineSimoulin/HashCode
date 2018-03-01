from tqdm import tqdm
import numpy as np
import random
from .util import get_ride_length, move_to

class Solution():
    def __init__(self, inst):
        self.inst = inst
        self.name = inst.name
        self.trajets = {} # key : vehicle id, value : list of Rides
        self.score = 0 # self.compute_solution_score()

    def check_insertion(self, vhl_id, new_ride, inplace=False):
        t=rides[0].a+rides[0].b
        pos_x = rides[0].a
        pos_y = rides[0].b
        for ri, r in enumerates(self.trajets[vhl_id]):
            # on a le temps d'aller jusqu'au ride suivant
            if can_take_ride(t, pos_x, pos_y, new_ride):
                # check possible to finish the ride before taking the next one
                ride_list = [new_ride] + self.trajets[vhl_id][ri:]
                if is_valid_rides_for_one_car(self.trajets[vhl_id]):
                    if inplace:
                        self.trajets[vhl_id].insert(new_ride.id)
                    return True
        return False

    def is_valid_rides_for_one_car(self, rides_list):
        is_valid = True
        pos_x, pos_y = 0, 0
        current_time = 0
        for ride in rides_list:
            # Go to position of start
            current_time, (pos_x, pos_y) = move_to(current_time, pos_x, pos_y, ride.a, ride.b)
            # Check that current time is after starting_time
            if current_time < ride.s:
                is_valid = False
            # Go to destination
            current_time, (pos_x, pos_y) = move_to(current_time, pos_x, pos_y, ride.x, ride.y)
            # Check that end time is before finish
            if current_time >= ride.f:
                is_valid = False

        return is_valid

    def update_solution_score(old_vhls_rides, new_vhls_rides):
        old_score = compute_score_subset(old_vhls_rides)
        new_score = compute_score_subset(new_vhls_rides)
        self.score += new_score
        self.score -= old_score

    def mutate(self, n=20):
        """
        mutate solution given voisinage.
        enlève au hasard jusqu'a n trajets puis les remplace.
        Jusqu'à n trajets peuvent être mutés
        """
        # keep trace of modifications
        old_vhls_rides = {}

        # choisi n véhicules au hasard
        vhl_ids = random.sample(self.trajets.keys(), n)

        for vhl_id in vhl_ids:
            # on leur enlève 1 trajet chacun au hasard, qu'on va remettre comme non done
            # a adapter
            removed_ride_idx = random.randint(len(self.trajets[vhl_id]))
            self.trajets[vhl_id][removed_ride_idx].done = False
            self.trajets[vhl_id][removed_ride_idx].pop(removed_ride_idx)

            # on attribue aux n véhicules un nouveau trajet si possible
            available_rides = [r for r in self.inst.rides if r.done=False]
            available_rides = available_rides.shuffle
            for r in available_rides:
                if check_insertion(vhl_id, r, inplace=True):
                    break

            # update solution and scores
            new_vhls_rides = dict(filter(lambda i:i[0] in validkeys, self.trajets.iteritems()))
            self.update_solution_score(old_vhls_rides, new_vhls_rides)

    def get_trajet_bonus(self, rides):
        t=rides[0].a+rides[0].b
        res = 0
        for ri, r in enumerate(rides):
            if t == r.s:
                res += self.inst.B
            # add ride time and time to get to next tide
            t += r.length
            t += abs(rides[ri+1].a-r.x) + abs(rides[ri+1].b - r.y)
        return res

        def compute_score_subset(self, trajet_subsets):
            s = 0
            for v_id, v_rides in trajet_subsets.items():
                for r in v_rides:
                    # add ride length
                    s += r.length
                    # check if bonus
                s += get_trajet_bonus(v_rides)
            return s

    def compute_solution_score(self):
        s = 0
        for v_id, v_rides in self.trajets.items():
            for r in rides:
                # cadd ride length
                s += r.length
                # check if bonus
            s += get_trajet_bonus(rides)
        self.score = s

    def write_solution(self, filepath):
        # sort the traject solution
        with open(filepath, 'w') as f:
            for v, traj in self.trajets.items():
                if len(traj):
                    out = str(len(traj)) + " " + " ".join(str(t.id) for t in traj)
                    f.write(out)
                    f.write('\n')
