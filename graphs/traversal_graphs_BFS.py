# Traversal Graphs using BFS

# Ex.:
# [[1, 3],
#  [0],
#  [3, 8]
#  [0, 2, 4, 5]
#  [3, 6]
#  [3]
#  [4, 7]
#  [6]
#  [2]] --> [0, 1, 3, 4, 5, 2, 6, 8, 7]

def bfs(arr):
    queue, result, seen = [0], [], set()
    while len(queue) > 0:
        cur_vertex = queue.pop(0)
        seen.add(cur_vertex)
        result.append(cur_vertex)
        for v in arr[cur_vertex]:
            if v not in seen:
                queue.append(v)
    return result


adj_list = [[1, 3], [0], [3, 8], [0, 4, 5, 2], [3, 6], [3], [4, 7], [6], [2]]
print(bfs(adj_list))
