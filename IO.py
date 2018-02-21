from utils import *

def write_solution(filepath, videos_on_cache):
    used_caches = 0
    for cache in videos_on_cache:
        if len(cache):
            used_caches += 1

    with open(filepath, 'w') as f:
        f.write(str(used_caches))
        f.write('\n')
        for idx, c in enumerate(videos_on_cache):
            if len(c):
                out = str(idx) + " " + " ".join(str(i) for i in c)
                f.write(out)
                f.write('\n')

def read_dataset(fpath):
    with open(fpath, 'r') as reader:
        # numbers
        n_vid, n_end, n_req, n_cache, s_cache = [int(i) for i in reader.readline().split(" ")]

        # video sizes
        s_videos = [int(i) for i in reader.readline().split(" ")]

        # endpoints
        endpoints = []
        for e in range(n_end):
            L_D, K = [int(i) for i in reader.readline().split(" ")]

            connections = []

            # iterate over the K connected caches
            for k in range(K):
                c, L_C = [int(i) for i in reader.readline().split(" ")]
                connections.append((c, L_C))

            endpoints.append(Endpoint(e, L_D, connections))

        # requests
        requests = []
        for r in range(n_req):
            R_v, R_e, R_n = [int(i) for i in reader.readline().split(" ")]
            requests.append(Request(R_v, R_e, R_n))

        return n_vid, n_end, n_req, n_cache, s_cache, s_videos, endpoints, requests
