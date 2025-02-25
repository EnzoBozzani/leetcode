class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    move: str
    longest: int
    current: int    

    def dfs(self, node: TreeNode, previous_move: str):
        self.current += 1

        if self.current > self.longest:
            self.longest = self.current

        temp = self.current

        if node.left is not None:
            if previous_move == 'L':
                self.current = 0

            self.dfs(node.left, 'L')
            self.current -= 1

        self.current = temp
        
        if node.right is not None:
            if previous_move == 'R':
                self.current = 0

            self.dfs(node.right, 'R')
            self.current -= 1

    def longestZigZag(self, root: TreeNode | None) -> int:
        self.longest = 0
        self.current = 0

        if root is None:
            return 0
        
        if root.left is not None:
            self.dfs(root.left, 'L')
        
        self.current = 0
        
        if root.right is not None:
            self.dfs(root.right, 'R')

        return self.longest
    

if __name__ == '__main__':
    solution = Solution()
                        
    arr = [1,1,None,1,1,None,None,1,1,1]

    root = TreeNode(1)
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(1)
    node5 = TreeNode(1)
    node6 = TreeNode(1)

    root.left = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    print(solution.longestZigZag(root))                   

