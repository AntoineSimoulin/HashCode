import sys
import numpy as np

from collections import namedtuple

Endpoint = namedtuple('Endpoint', ['id', 'lat', 'con'])
Request = namedtuple('Request', ['vid', 'eid', 'n'])
Scoring = namedtuple('Scoring', ['vid', 'cid', 'score'])


def csv_print(mat, fmt='%.5f'):
    np.savetxt(sys.stdout.buffer, mat, fmt=fmt, newline="\n")

def compute_solution_score(videos_on_cache, requests, endpoints):
    score = 0.0
    total_req = 0

    for req in tqdm(requests, desc="Computing score"):
        # find caches that are connected to eid and have vid
        _lats = [endpoints[req.eid].lat]

        # check if video vid is on cache
        for _ci, _c in enumerate(videos_on_cache):
            if req.vid in _c:
                # check if endpoint eid is connected to cache
                for _cc in endpoints[req.eid].con:
                    if _ci == _cc[0]:
                        _lats.append(_cc[1])

        min_lat = np.min(_lats)
        diff_lat = endpoints[req.eid].lat - min_lat
        saved_lad = req.n * diff_lat
        score += saved_lad
        total_req += req.n

    return np.floor(score * 1000.0 / total_req)
