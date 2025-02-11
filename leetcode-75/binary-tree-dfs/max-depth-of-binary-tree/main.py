class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:        
    def maxDepth(self, node: TreeNode | None) -> int:
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1
    
        left_depth = 1
        right_depth = 1

        if node.left is not None:
            left_depth += self.maxDepth(node.left)
        if node.right is not None:
            right_depth += self.maxDepth(node.right)

        return left_depth if left_depth > right_depth else right_depth


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4

    print(solution.maxDepth(root))                          

