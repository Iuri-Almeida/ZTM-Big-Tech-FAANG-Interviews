# Course Scheduler - Topological Sort

# Ex.:
# numCourses = 2, prerequisites = [[1, 0]] → true
# numCourses = 2, prerequisites = [[1, 0], [0, 1]] → false
# numCourses = 6, prerequisites = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]] → true
# numCourses = 7, prerequisites = [[0, 3], [1, 0], [2, 1], [4, 5], [6, 4], [5, 6]] → false
# numCourses = 0, prerequisites = [] → true


# O(n + pairs) - Time Complexity
# O(n) - Space Complexity
def _adjacent_list(n, pre_reqs):
    adj_list = []
    for _ in range(n):
        adj_list.append([])
    for req in pre_reqs:
        adj_list[req[1]].append(req[0])
    return adj_list


# O(n + pairs) - Time Complexity
# O(n) - Space Complexity
def _create_in_degree(n, req):
    in_degree = [0] * n
    for r in req:
        in_degree[r[0]] += 1
    return in_degree


# O(n² + pairs) - Time Complexity
# O(n²) - Space Complexity
def course_scheduler(n, pre_reqs):
    graph, in_degree, total_in_degrees = _adjacent_list(n, pre_reqs), _create_in_degree(n, pre_reqs), len(pre_reqs)
    while total_in_degrees > 0 and 0 in in_degree:
        cur_idx = in_degree.index(0)
        in_degree[cur_idx] = -1
        total_in_degrees -= len(graph[cur_idx])
        for v in graph[cur_idx]:
            in_degree[v] -= 1
    return total_in_degrees == 0


total = 0
reqs = []
print(course_scheduler(total, reqs))
