class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    root1_leafs: list[int]
    root2_leafs: list[int]

    def __init__(self):
        self.root1_leafs = []
        self.root2_leafs = []

    def leaf_value(self, node: TreeNode | None, root: int):
        if node is None:
            return False

        if node.left is None and node.right is None:
            if root == 1:
                self.root1_leafs.append(node.val)
            else:
                self.root2_leafs.append(node.val)
            
            return

        if node.left is not None:
            self.leaf_value(node.left, root)
        
        if node.right is not None:
            self.leaf_value(node.right, root)
         
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        self.leaf_value(root1, 1)
        self.leaf_value(root2, 2)

        tree1_len = len(self.root1_leafs)
        tree2_len = len(self.root2_leafs)

        if tree1_len != tree2_len:
            return False

        for i in range(tree1_len):
            leaf1 = self.root1_leafs[i]
            leaf2 = self.root2_leafs[i]

            if leaf1 != leaf2:
                return False
            
        return True



if __name__ == '__main__':
    solution = Solution()

    root1 = TreeNode(3)
    node11 = TreeNode(5)
    node12 = TreeNode(1)
    node13 = TreeNode(6)
    node14 = TreeNode(2)
    node15 = TreeNode(9)
    node16 = TreeNode(8)
    node17 = TreeNode(7)
    node18 = TreeNode(4)

    root1.left = node11
    root1.right = node12
    node11.left = node13
    node11.right = node14
    node14.left = node17
    node14.right = node18
    node12.left = node15
    node12.right = node16

    root2 = TreeNode(3)
    node21 = TreeNode(5)
    node22 = TreeNode(1)
    node23 = TreeNode(6)
    node24 = TreeNode(7)
    node25 = TreeNode(4)
    node26 = TreeNode(2)
    node27 = TreeNode(9)
    node28 = TreeNode(8)

    root2.left = node21
    root2.right = node22
    node21.left = node23
    node21.right = node24
    node22.left = node25
    node22.right = node26
    node26.left = node27
    node26.right = node28

    print(solution.leafSimilar(root1, root2))                      

