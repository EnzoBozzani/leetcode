from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    num_of_sums: int
    target_sum: int
    hashmap: defaultdict

    def __init__(self):
        self.num_of_sums = 0
        self.hashmap = defaultdict(int)
        self.hashmap[0] = 1

    def sum(self, node: TreeNode | None, current: int):        
        current += node.val

        self.num_of_sums += self.hashmap[current - self.target_sum]

        self.hashmap[current] += 1

        if node.left is not None:
            self.sum(node.left, current)
        
        if node.right is not None:
            self.sum(node.right, current)

        self.hashmap[current] -= 1
        
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        self.target_sum = targetSum

        if root is None:
            return 0

        self.sum(root, 0)
        
        return self.num_of_sums

if __name__ == '__main__':
    solution = Solution()
                        
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(-3)
    node3 = TreeNode(3)
    node4 = TreeNode(2)
    node5 = TreeNode(11)
    node6 = TreeNode(3)
    node7 = TreeNode(-2)
    node8 = TreeNode(1)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.right = node8

    print(solution.pathSum(root, 8))                   

