import circuit
import random

class Solution():
    def __init__(self, inst):
        self.inst = inst
        self.name = inst.name

        self.circuits = []
        self.remorques = inst.remorques

        self.length = 9999999
        self.desequilibre = 9999999


    def update(self):
        self.length = sum([self.circuits[i].length for i in xrange(len(self.circuits))])
        self.desequilibre = sum([self.circuits[i].desequilibre for i in xrange(len(self.circuits))])


    def is_valid(self):
        validity = True
        for c in self.circuits:
            if len(c.stations) == 0:
                validity = False
        if len(self.circuits) == 0:
            validity = False
        return validity

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

    def to_file(self, filename):
        f = open(filename, 'w')
        f.write('# générée le : TODO\n\n')
        f.write('nom '+self.name+'\n')
        f.write('desequilibre '+str(self.desequilibre)+'\n')
        f.write('distance '+str(self.length)+'\n\n')
        for c in self.circuits:
            f.write(c.to_string())
        f.close()

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

    def to_string_long(self):
        print '# générée le : TODO\n\n'
        print 'nom '+self.name+'\n'
        print 'desequilibre '+str(self.desequilibre)+'\n'
        print 'distance '+str(self.length)+'\n\n'
        for c in self.circuits:
            print c.to_string()

    def to_string(self):
        print 'desequilibre '+str(self.desequilibre)+'\n'
        print 'distance '+str(self.length)+'\n\n'

    def best_voisinage(self):
        for j in xrange(len(self.remorques)):
            self.circuits[j].mutate_2opt_best()
        self.update()
