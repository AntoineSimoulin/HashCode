from collections import namedtuple
# import sys
# import numpy as np

Endpoint = namedtuple('Endpoint', ['id', 'lat', 'con'])
Request = namedtuple('Request', ['vid', 'eid', 'n'])
Scoring = namedtuple('Scoring', ['vid', 'cid', 'score'])


class Instance:
    def __init__(self, fpath, name='instance'):
        self.fpath = fpath
        self.read_dataset()
        self.name = name

    def read_dataset(self):
        with open(self.fpath, 'r') as f:

            # numbers
            self.n_vid, self.n_end, self.n_req, self.n_cache, self.s_cache = \
                [int(i) for i in f.readline().split(" ")]

            # video sizes
            self.s_videos = [int(i) for i in f.readline().split(" ")]

            # endpoints
            self.endpoints = []
            for e in range(self.n_end):
                L_D, K = [int(i) for i in f.readline().split(" ")]

                connections = []

                # iterate over the K connected caches
                for k in range(K):
                    c, L_C = [int(i) for i in f.readline().split(" ")]
                    connections.append((c, L_C))

                self.endpoints.append(Endpoint(e, L_D, connections))

            # requests
            self.requests = []
            for r in range(self.n_req):
                R_v, R_e, R_n = [int(i) for i in f.readline().split(" ")]
                self.requests.append(Request(R_v, R_e, R_n))

            # return n_vid, n_end, n_req, n_cache, s_cache, s_videos, endpoints, requests

    # def __repr__(self):
    #     return "n_vid : %i" %self.n_vid

    def __str__(self):
        return "Instance name : %s \nn_vid : %i\nn_end : %i\nn_req : %i\nn_cache : %i\ns_cache : %i" %(self.name, self.n_vid, self.n_end, self.n_req, self.n_cache, self.s_cache)
