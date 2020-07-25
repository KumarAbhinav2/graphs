from collections import defaultdict
from datetime import datetime as dt


def duration(func):
    def wrapped(*args, **kwargs):
        start = dt.now()
        res = func(*args)
        print(f"time taken in microseconds by {func.__name__} ", (dt.now()-start).microseconds)
        return res
    return wrapped


class Graph:
    """Graph implementation using dictionary and adjacency list concept
        Structure will resemble something like this,
        {
            'A': ['B', 'C'],
            'B': ['D', 'E']
            'D': ['F']
        }

    """

    def __init__(self, directed):
        self.directed = directed
        self.adjList = defaultdict(list)

    def add_edge(self, src, dest):
        self.adjList[src].append(dest)
        if not self.directed:
            self.adjList[dest].append(src)


class Queue:

    def __init__(self):
        self.queue_list = []

    def front(self):
        if self.isEmpty():
            return None
        return self.queue_list[0]

    def isEmpty(self):
        if len(self.queue_list) == 0:
            return True
        return False

    def enqeue(self, elem):
        self.queue_list.append(elem)

    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        return front




