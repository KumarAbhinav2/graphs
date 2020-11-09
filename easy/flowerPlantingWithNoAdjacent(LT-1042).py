"""
Algo1:
1) Create a three sequences to
    1) To hold gardens (represent each element as set of (1, 2, 3, 4) which represents all possible flowers initially at
        each garden)
    2) To hold flowers (blank)
    3) To represent graph (can be dict of list, represented as adjcency list)
2) Iterate through the give number of gardens
    1) for each iteration, fetch first available flower from corresponding garden (i.e for first iteration fetch 1 from set of
        (1, 2, 3, 4)) and add it to the flowers list.
    2) Get all the neighbours of current garden, and iterate through each again
        1) for each neighbour garden remove the flower which is being taken already by the src garden.
3) Finally return the flowers list
"""
from collections import defaultdict
from graph import duration

class Solution:

    @duration
    def gardenNoAdj_algo1(self, N, paths):
        gardens = [set([1, 2, 3, 4]) for i in range(N)]  # garden list
        flowers = []  # flowers
        gardens_graph = defaultdict(list)  # garden_graph
        for src, dest in paths:
            gardens_graph[src - 1].append(dest)
            gardens_graph[dest - 1].append(src)

        for garden in range(N):
            flowers.append(gardens[garden].pop())  # adding flowers
            for neigh_garden in gardens_graph[garden]:
                gardens[neigh_garden - 1].discard(
                    flowers[garden])  # source already has that flower so remove it from available set
        return flowers

    @duration
    def gardenNoAdj_algo1_faster(self, N, paths):
        g, t, f = [set([1, 2, 3, 4]) for i in range(N)], [[] for i in range(N)], []
        for i in paths: t[i[0]-1].append(i[1]),t[i[1]-1].append(i[0])
        for i in range(N):
            f.append(g[i].pop())
            for j in t[i]: g[j-1].discard(f[i])
        return f


    @duration
    def gardenNoAdj_algo2(self, N, paths):
        flowers = [0]*N
        garden = defaultdict(list)
        for src,dst in paths:
            garden[src].append(dst)
            garden[dst].append(src)
        for i in range(1, N+1):
            colors = set([1,2,3,4])
            for neigh in garden[i]:
                if flowers[neigh-1] in colors:
                    colors.remove(flowers[neigh-1])
            flowers[i-1] = colors.pop()
        return flowers

obj = Solution()
paths = [[1,2], [1, 3], [2, 4,] ,[2, 5], [3, 5], [3, 6], [4, 5]]
print(obj.gardenNoAdj_algo1(6, paths))
print(obj.gardenNoAdj_algo2(6, paths))
print(obj.gardenNoAdj_algo1_faster(6, paths))