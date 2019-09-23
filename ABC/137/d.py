import heapq


class Job:

    def __repr__(self):
        return "{0},{1}".format(self.days, self.reward)

    def __lt__(self, other):
        return self.reward < other.reward

    def __init__(self, job_id, reward, days):
        self.id = job_id
        self.reward = reward
        self.days = days

N, M = list(map(int, input().split()))
h = []
jobs = []

for i in range(N):
    A, B = list(map(int, input().split()))
    jobs.append(Job(job_id=i, reward=B, days=A))


jobs = sorted(jobs, key=lambda j: j.days)
idx = 0
c = 0

for i in range(1, M+1):
    while idx < N and jobs[idx].days <= i:
        heapq.heappush(h, -jobs[idx].reward)
        idx += 1

    # print(i)
    if len(h) != 0:
        # print(h)
        c += -heapq.heappop(h)

print(c)
