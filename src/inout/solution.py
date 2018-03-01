from tqdm import tqdm
import numpy as np
import random
from util import get_ride_length, move_to

class Solution():
    def __init__(self, inst):
        self.inst = inst
        self.name = inst.name
        self.trajets = []
        self.score = 0 # self.compute_solution_score()

    def mutate_a(self):
        """
        mutate solution given voisinage a :
        remove a random video from the cache. Consider all video from the data
        center that fit in the cache and insert it. If no video fit, a new
        random video is taken out of the cache.
        Update score and videos on cache
        """
        i = random.randrange(self.inst.n_cache) # get random cache
        j = random.randrange(len(self.videos_on_cache[i])) # get random video index in cache
        self.videos_on_cache[i][j], self.videos_on_cache[i][-1] = self.videos_on_cache[i][-1], self.videos_on_cache[i][j] # swap with the last element
        self.videos_on_cache[i] = self.videos_on_cache[i][:-1]  # remove last element


        # check available videos
        v_size = [v for vi,v in enumerate(self.inst.s_videos) if vi in self.videos_on_cache[i]]
        v_size_tot = sum(v_size)
        possible_v = [v for k,v in enumerate(self.inst.s_videos) if k <= (self.inst.s_cache-v_size_tot)]
        choosen_v = random.choice(possible_v)

        # update solution and scores
        self.videos_on_cache[i].append(choosen_v)
        self.compute_solution_score()

    def is_valid(self, rd1, rd2):
        """
        check total video size in each cache does not exceed limits
        """
        for _ci, _c in enumerate(self.videos_on_cache):
            v_size = [_v for _vi, _v in enumerate(self.inst.s_videos) if _vi in _ci]
            v_size_tot = sum(v_size)
            if _c.s_cache < v_size_tot:
                return False
        return True

    def get_trajects_bonus(self, rides):
        t=rides[0].a+rides[0].b
        res = 0
        for ri, r in enumerates(rides):
            if t == r.s:
                res += self.inst.B
            # add ride time and time to get to next tide
            t += r.length
            t += abs(rides[ri+1].a-r.x) + abs(rides[ri+1].b - y)
        return res

    def compute_solution_score(self):
        s = 0
        for v_id, v_rides in self.trajets.items():
            for r in rides:
                # check if ride is valid
                if self.is_valid(rd1, rd2):
                    s += r.length
                # check if bonus
            s += get_trajects_bonus(self, rides)
        self.score = score

    def write_solution(self, filepath):
        # sort the traject solution
        with open(filepath, 'w') as f:
            for v, traj in self.trajets.items():
                if len(traj):
                    out = str(len(traj)) + " " + " ".join(str(t.id) for t in traj)
                    f.write(out)
                    f.write('\n')
