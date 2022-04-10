# Monarchy
# Question: Given the following interface, implement its methods.
# interface Monarchy {
#   void birth(String child, String parent);
#   void death(String name);
#   List<String> getOrderOfSuccession();
# }

# Ex.:
#           Jake
#        /   |   \
#     Cath  Tom  Cel
#    /   \        |
#  Jane  Mark   Peter
#   |
# Sarah


# O(children) - Space Complexity
class TreeNode(object):
    def __init__(self, parent):
        self.__parent = parent
        self.__is_dead = False
        self.__children = []

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def name(self):
        return self.__parent

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def children(self):
        return self.__children

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def is_dead(self):
        return self.__is_dead

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def set_death(self):
        self.__is_dead = True

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def add_child(self, child):
        self.__children.append(child)


# O(nodes) - Space Complexity
class Monarchy(object):
    def __init__(self, king):
        self.__king = TreeNode(king)
        self.__nodes = {self.__king.name(): self.__king}

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def __get_node_by_name(self, name):
        if name in self.__nodes:
            return self.__nodes[name]
        raise RuntimeError(f"The node name '{name}' does not exists.")

    # O(n) - Time Complexity
    # O(log n) - Space Complexity
    def __dfs(self, cur_node, arr):
        if not cur_node.is_dead():
            arr.append(cur_node.name())

        for child in cur_node.children():
            self.__dfs(child, arr)

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def birth(self, child, parent):
        new_child = TreeNode(child)

        node_parent = self.__get_node_by_name(parent)
        node_parent.add_child(new_child)

        self.__nodes[new_child.name()] = new_child

    # O(1) - Time Complexity
    # O(1) - Space Complexity
    def death(self, name):
        death_node = self.__get_node_by_name(name)
        death_node.set_death()

    # O(n) - Time Complexity
    # O(log n) - Space Complexity
    def get_order_of_succession(self):
        arr = []
        self.__dfs(self.__king, arr)
        return arr


mon = Monarchy('Jake')
mon.birth('Cath', 'Jake')
mon.birth('Tom', 'Jake')
mon.birth('Cel', 'Jake')
mon.birth('Jane', 'Cath')
mon.birth('Mark', 'Cath')
mon.birth('Sarah', 'Jane')
mon.birth('Peter', 'Cel')
print(mon.get_order_of_succession())
mon.death('Jake')
mon.death('Jane')
print(mon.get_order_of_succession())
