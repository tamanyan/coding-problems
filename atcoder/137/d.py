import math
from itertools import accumulate
from typing import List, Set


class Job:

    def __repr__(self):
        return f'Job(reward={self.reward}, days={self.days})'

    def __init__(self, reward: int, days: int):
        self.reward = reward
        self.days = days


def dfs(jobs: Set[Job], remaing_days: int, selected_jobs: Set[Job]) -> int:
    reward = 0

    # print(jobs, remaing_days)

    if remaing_days == 0:
        return 0

    for job in jobs:
        if job.days <= remaing_days:
            print(
                f'trying {job} sum: {reward} remaing_days:{remaing_days} selected:{selected_jobs}')

            next_selected_jobs = selected_jobs | set([job])
            remaining_jobs = jobs - set([job])
            new_reward = job.reward + \
                dfs(remaining_jobs, remaing_days - 1, next_selected_jobs)

            if reward < new_reward:
                print(
                    f'pickup {job} sum: {new_reward} remaing_days:{remaing_days} selected:{selected_jobs}')

            reward = max(reward, new_reward)
        else:
            print(
                f'fail to pickup {job} sum: {reward} remaing_days:{remaing_days} selected:{selected_jobs}')

    return reward


N, M = list(map(int, input().split()))
jobs: Set[Job] = set()

for i in range(N):
    A, B = list(map(int, input().split()))
    jobs.add(Job(reward=B, days=A))

print(dfs(jobs, M, set()))
