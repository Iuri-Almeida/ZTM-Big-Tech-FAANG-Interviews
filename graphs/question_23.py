# Time Needed to Inform All Employees
# Question: A company has n employees with unique IDs from 0 to n - 1. The head of the company has the ID headID.
#
# You will receive a managers array where managers[i] is the ID of the manager for employee i. Each employee has one
# direct manager. The company head has no manager (managers[headID] = -1). It’s guaranteed the subordination
# relationships will have a tree structure.
#
# The head of the company wants to inform all employees of the news. He will inform his direct subordinates who will
# inform their direct subordinates and so on until everyone knows the news.
#
# You will receive an informTime array where informTime[i] is the time it takes for employee i to inform all their
# direct subordinates. Return the total number of minutes it takes to inform all employees of the news.

# Ex.:
# n = 1, headID = 0, manager = [-1], informTime = [0] --> 0
# n = 6, headID = 2, manager = [2, 2, -1, 2, 2, 2], informTime = [0, 0, 1, 0, 0, 0] --> 1
# n = 8, headID = 1, manager = [1, -1, 1, 0, 0, 4, 2, 6], informTime = [3, 10, 2, 0, 4, 0, 1, 0] --> 17
# n = 15, head_id = 0, manager = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
# informTime = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0] --> 3


# O(n) - Time Complexity
# O(n) - Space Complexity
def __dfs(graph, cur_id, inform_time, max_minutes=0, minutes=0):
    max_minutes = max(max_minutes, minutes + inform_time[cur_id])
    for sub_id in graph[cur_id]:
        max_minutes = max(max_minutes, __dfs(graph, sub_id, inform_time, max_minutes, minutes + inform_time[cur_id]))
    return max_minutes


# O(n) - Time Complexity
# O(n) - Space Complexity
def __dfs_02(graph, cur_id, inform_time):
    if len(graph[cur_id]) == 0:
        return 0
    max_minutes = 0
    for sub_id in graph[cur_id]:
        max_minutes = max(max_minutes, __dfs_02(graph, sub_id, inform_time))
    return max_minutes + inform_time[cur_id]


# O(n) - Time Complexity
# O(n) - Space Complexity
def _adjacent_list(n, manager):
    g = []
    for _ in range(n):
        g.append([])
    for i in range(n):
        if manager[i] == -1:
            continue
        g[manager[i]].append(i)
    return g


# O(n) - Time Complexity
# O(n) - Space Complexity
def inform_all_employees(n, head_id, manager, inform_time):
    graph = _adjacent_list(n, manager)
    return __dfs_02(graph, head_id, inform_time)


employees = 8
headID = 4
managers = [2, 2, 4, 6, -1, 4, 4, 5]
informTime = [0, 0, 4, 0, 7, 3, 6, 0]
print(inform_all_employees(employees, headID, managers, informTime))
