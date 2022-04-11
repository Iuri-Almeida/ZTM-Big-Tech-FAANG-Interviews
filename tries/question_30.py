# Implement Trie (Prefix Tree)
# Question: Implement a Trie with insert, search and startsWith methods.
# interface Trie {
#   void insert(String word);
#   Boolean search(String word);
#   Boolean startsWith(String prefix);
# }

# Ex.:
# insert('apple'), insert('dog'), insert('app')
#      root
#     /    \
#    a      d
#   /        \
#  p         o
#  \          \
#   p (end)    g (end)
#    \
#     l
#      \
#       e (end)


class TreeNode(object):
    def __init__(self):
        self.__children = dict()
        self.__end = False

    def add_child(self, child):
        self.__children[child] = TreeNode()

    def end(self):
        return self.__end

    def set_end(self):
        self.__end = True

    def get_child(self, name):
        if self.check_child(name):
            return self.__children[name]
        raise RuntimeError(f"The name '{name}' does not exists.")

    def check_child(self, child):
        return child in self.__children


# O(word) - Time Complexity
# O(word) - Space Complexity
class TrieIterative(object):
    def __init__(self):
        self.__root = TreeNode()

    def insert(self, word):
        cur_node = self.__root
        for i in range(len(word)):
            cur_char = word[i]
            if not cur_node.check_child(cur_char):
                cur_node.add_child(cur_char)
            cur_node = cur_node.get_child(cur_char)
        cur_node.set_end()

    def search(self, word):
        cur_node = self.__root
        for i in range(len(word)):
            cur_char = word[i]
            if not cur_node.check_child(cur_char):
                return False
            cur_node = cur_node.get_child(cur_char)
            if cur_node.end() and i == len(word) - 1:
                return True
        return False

    def starts_with(self, prefix):
        cur_node = self.__root
        for i in range(len(prefix)):
            cur_char = prefix[i]
            if not cur_node.check_child(cur_char):
                return False
            cur_node = cur_node.get_child(cur_char)
        return True


# O(word) - Time Complexity
# O(word) - Space Complexity
class TrieRecursive(object):
    def __init__(self):
        self.__root = TreeNode()

    def insert(self, word):
        return self.__recursive_insert(word, self.__root)

    def __recursive_insert(self, word, cur_node):
        if len(word) == 0:
            cur_node.set_end()
            return
        elif not cur_node.check_child(word[0]):
            cur_node.add_child(word[0])
        self.__recursive_insert(word[1:], cur_node.get_child(word[0]))

    def search(self, word):
        return self.__recursive_search(word, self.__root)

    def __recursive_search(self, word, cur_node):
        if cur_node.end() and len(word) == 0:
            return True
        elif len(word) == 0:
            return False
        elif not cur_node.check_child(word[0]):
            return False
        return self.__recursive_search(word[1:], cur_node.get_child(word[0]))

    def starts_with(self, prefix):
        return self.__recursive_starts_with(prefix, self.__root)

    def __recursive_starts_with(self, prefix, cur_node):
        if len(prefix) == 0:
            return True
        elif not cur_node.check_child(prefix[0]):
            return False
        return self.__recursive_starts_with(prefix[1:], cur_node.get_child(prefix[0]))


trie = TrieIterative()
trie.insert('apple')
print(f"Search 'dog' BEFORE insertion: {trie.search('dog')}")
trie.insert('dog')
print(f"Search 'dog' AFTER insertion: {trie.search('dog')}")
print(f"Starts with 'app': {trie.starts_with('app')}")
print(f"Search 'app' BEFORE insertion: {trie.search('app')}")
trie.insert('app')
print(f"Search 'app' AFTER insertion: {trie.search('app')}")

print("-" * 40)

trie_rec = TrieRecursive()
trie_rec.insert('apple')
print(f"Search 'dog' BEFORE insertion: {trie_rec.search('dog')}")
trie_rec.insert('dog')
print(f"Search 'dog' AFTER insertion: {trie_rec.search('dog')}")
print(f"Starts with 'app': {trie_rec.starts_with('app')}")
print(f"Search 'app' BEFORE insertion: {trie_rec.search('app')}")
trie_rec.insert('app')
print(f"Search 'app' AFTER insertion: {trie_rec.search('app')}")
