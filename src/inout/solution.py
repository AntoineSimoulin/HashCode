# import circuit
# import @

class Solution():
    def __init__(self, inst):
        self.inst = inst
        self.name = inst.name
        self.videos_on_cache = []

    def is_valid(self):
        """
        check total video size in each cache does not exceed limits
        """
        for _ci, _c in enumerate(self.videos_on_cache):
            v_size = [v for _vi, _v in enumerate(inst.s_videos) if _vi in inst.s_videos]
            v_size_tot = sum(v_size)
            if _c.s_cache < v_size_tots:
                return False
        return True

    def compute_solution_score(self):
        score = 0.0
        total_req = 0

        for req in tqdm(requests, desc="Computing score"):
            # find caches that are connected to eid and have vid
            _lats = [self.inst.endpoints[req.eid].lat]

            # check if video vid is on cache
            for _ci, _c in enumerate(self.videos_on_cache):
                if req.vid in _c:
                    # check if endpoint eid is connected to cache
                    for _cc in self.inst.endpoints[req.eid].con:
                        if _ci == _cc[0]:
                            _lats.append(_cc[1])

            min_lat = np.min(_lats)
            diff_lat = self.inst.endpoints[req.eid].lat - min_lat
            saved_lad = req.n * diff_lat
            score += saved_lad
            total_req += req.n

        return np.floor(score * 1000.0 / total_req)

    def write_solution(self, filepath):
        used_caches = 0
        for cache in self.videos_on_cache:
            if len(cache):
                used_caches += 1

        with open(filepath, 'w') as f:
            f.write(str(used_caches))
            f.write('\n')
            for idx, c in enumerate(self.videos_on_cache):
                if len(c):
                    out = str(idx) + " " + " ".join(str(i) for i in c)
                    f.write(out)
                    f.write('\n')
