def dfs(graph, node, path, result, target):
    if node == target:
        result.append(list(path))
        return

    for neighbor in graph[node]:
        path.append(neighbor)
        dfs(graph, neighbor, path, result, target)
        path.pop()


def all_paths_source_target(graph):
    result = []
    target = len(graph) - 1
    dfs(graph, 0, [0], result, target)
    return result


def main():
    test_cases = [
        [[1, 2], [3], [3], []],
        [[4, 3, 1], [3, 2, 4], [3], [4], []],
        [[1], [2], [3], []],
        [[1, 2], [3], [3], [4], []],
        [[1], [2], [], []]
    ]

    for i, graph in enumerate(test_cases, 1):
        output = all_paths_source_target(graph)
        print(i, ".\t graph:", graph, sep="")
        print("\t output:",output)
        print("-" * 100)

if __name__ == "__main__":
    main()