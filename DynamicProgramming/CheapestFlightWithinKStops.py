"""
https://leetcode.com/explore/featured/card/graph/622/single-source-shortest-path-algorithm/3864/

https://leetcode.com/explore/featured/card/graph/622/single-source-shortest-path-algorithm/ -- good source of reference
follow above explanation
Idea behind how this problem is solved

Although the “Bellman-Ford algorithm” cannot find the shortest path in a graph with “negative weight cycles”,
it can detect whether there exists a “negative weight cycle” in the “graph”.

Detection method: After relaxing each edge N-1 times, perform the Nth relaxation.
 According to the “Bellman-Ford algorithm”, all distances must be the shortest after relaxing each edge N-1 times.
 However, after the Nth relaxation, if there exists distances[u] + weight(u, v) < distances(v) for any edge(u, v), it means there is a shorter path .
  At this point, we can conclude that there exists a “negative weight cycle”.
"""
from math import inf


def findCheapestFlight(n, flights, src, dst, k):
    dist = [inf] * n
    dist[src] = 0

    for _ in range(k+1):
        new_dist = dist[:]

        for u, v, w in flights:

            if dist[u] != inf and dist[u] + w < new_dist[v]:
                new_dist[v] = dist[u] + w


        dist = new_dist

    return -1 if dist[dst] == inf else dist[dst]

def main():
    tests = get_input_test_cases()

    for i , (n, flights, src, dst, k) in enumerate(tests):
        print("\t flights : ", flights)
        print("\t source :", src)
        print("\t destination :", dst)

        result = findCheapestFlight(n, flights, src, dst, k)
        print("cheapest flight is :", result)
        print("-"*100)

def get_input_test_cases():
    return [
            (
                4,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                    [2, 3, 100],
                    [0, 3, 500],
                ],
                0,
                3,
                2,
            ),
            (
                3,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                ],
                0,
                2,
                0,
            ),
            (
                5,
                [
                    [0, 1, 200],
                    [0, 2, 500],
                    [1, 2, 100],
                    [1, 3, 300],
                    [2, 3, 100],
                    [3, 4, 50],
                    [0, 4, 1000],
                ],
                0,
                4,
                3,
            ),
            (
                3,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                ],
                1,
                1,
                1,
            ),
            (
                4,
                [
                    [0, 1, 100],
                    [1, 2, 100],
                ],
                0,
                3,
                2,
            ),
    ]


if __name__ == "__main__":
    main()