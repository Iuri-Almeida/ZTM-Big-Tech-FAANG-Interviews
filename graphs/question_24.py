# Course Scheduler
# Question: There are a total of n courses to take, labeled from 0 to n - 1.
#
# Some courses have prerequisite courses. This is expressed as a pair i.e. [1, 0] which indicates you must take course
# 0 before taking course 1.
#
# Given the total number of courses and an array of prerequisite pairs, return if it is possible to finish all courses.

# Ex.:
# numCourses = 2, prerequisites = [[1, 0]] → true
# numCourses = 2, prerequisites = [[1, 0], [0, 1]] → false
# numCourses = 6, prerequisites = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]] → true
# numCourses = 7, prerequisites = [[0, 3], [1, 0], [2, 1], [4, 5], [6, 4], [5, 6]] → false
# numCourses = 0, prerequisites = [] → true


# O(n²) - Time Complexity
# O(n) - Space Complexity
def __bfs(graph, cur_node):
    queue, seen = graph[cur_node], set()
    while len(queue) > 0:
        cur_vertex = queue.pop(0)
        seen.add(cur_vertex)
        if cur_vertex == cur_node:
            return False
        for v in graph[cur_vertex]:
            if v not in seen:
                queue.append(v)
    return True


# O(n) - Time Complexity
# O(n) - Space Complexity
def _adjacent_list(n, pre_reqs):
    adj_list = []
    for _ in range(n):
        adj_list.append([])
    for req in pre_reqs:
        adj_list[req[1]].append(req[0])
    return adj_list


# O(pairs + n³) - Time Complexity
# O(n²) - Space Complexity
def course_scheduler(n, pre_reqs):
    graph = _adjacent_list(n, pre_reqs)
    for node in range(n):
        if not __bfs(graph, node):
            return False
    return True


total = 6
reqs = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
print(course_scheduler(total, reqs))
