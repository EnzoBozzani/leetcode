class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    p_ancestors: list[int]
    stop: bool
    stop_2: bool
    common: TreeNode

    def dfs_p(self, node: TreeNode | None, p_value: int):
        if node is None: 
            return
    
        if node.val == p_value:
            self.stop = True

        if not self.stop:
            self.dfs_p(node.left, p_value)

        if not self.stop:
            self.dfs_p(node.right, p_value)

        if self.stop:
            self.p_ancestors.append(node.val)
            return
    
    def dfs_q(self, node: TreeNode | None, q_value: int):
        if node is None or self.stop_2: 
            return
            
        if node.val == q_value:
            self.stop = True

        if not self.stop and not self.stop_2:
            self.dfs_q(node.left, q_value)
        
        if not self.stop and not self.stop_2:
            self.dfs_q(node.right, q_value)

        if not self.stop_2 and self.stop and node.val in self.p_ancestors:
            self.common = node
            self.stop_2 = True
            return

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p_ancestors = []
        self.stop = False
        self.stop_2 = False

        self.dfs_p(root, p.val)

        self.stop = False

        self.dfs_q(root, q.val)

        return self.common

if __name__ == '__main__':
    solution = Solution()
                        
    root = TreeNode(3)
    node1 = TreeNode(5)    
    node2 = TreeNode(1) 
    node3 = TreeNode(6)  
    node4 = TreeNode(2) 
    node5 = TreeNode(0)  
    node6 = TreeNode(8)
    node7 = TreeNode(7)  
    node8 = TreeNode(4)  

    root.left = node1
    root.right = node2  
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    node4.left = node7
    node4.right = node8

    print(solution.lowestCommonAncestor(root, node1, node8).val)             

