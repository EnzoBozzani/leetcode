class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    good_nodes: int
    max: list[int]

    def __init__(self):
        self.good_nodes = 0
        self.max = [(-10**4) - 1]

    def is_good_node(self, node: TreeNode):
        is_max = False

        if node.val >= self.max[-1]:
            self.good_nodes += 1
            self.max.append(node.val)
            is_max = True

        if node.left is not None:
            self.is_good_node(node.left)
        
        if node.right is not None:
            self.is_good_node(node.right)

        if is_max:
            self.max.pop()

    def goodNodes(self, root: TreeNode) -> int:
        self.is_good_node(root)

        return self.good_nodes
        


if __name__ == '__main__':
    solution = Solution()
                        
    root = TreeNode(3)
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = TreeNode(3)
    node4 = TreeNode(1)
    node5 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5

    print(solution.goodNodes(root))                     

