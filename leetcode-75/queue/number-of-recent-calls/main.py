class RecentCounter:
    counter: int
    requests: list[int]

    def __init__(self):
        self.counter = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.counter += 1

        while(True):
            r = self.requests[0]

            if t - 3000 > r:
                self.requests.pop(0)
                self.counter -= 1
            else:
                break

        return self.counter
        

obj = RecentCounter()
examples = [[642,1849,4921,5936,5957]]

for e in examples:
    for n in e:
        print(obj.ping(n))