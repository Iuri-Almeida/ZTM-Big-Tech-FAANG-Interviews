# Traversal Graphs using DFS

# Ex.:
# [[1, 3],
#  [0],
#  [3, 8]
#  [0, 2, 4, 5]
#  [3, 6]
#  [3]
#  [4, 7]
#  [6]
#  [2]] --> [0, 1, 3, 4, 6, 7, 5, 2, 8]


def __dfs(arr, result, seen, vertex=0):
    if vertex in seen:
        return
    seen.add(vertex)
    result.append(vertex)
    for v in arr[vertex]:
        __dfs(arr, result, seen, v)


def traverse(arr):
    result, seen = [], set()
    __dfs(arr, result, seen)
    return result


adj_list = [[1, 3], [0], [3, 8], [0, 4, 5, 2], [3, 6], [3], [4, 7], [6], [2]]
print(traverse(adj_list))
