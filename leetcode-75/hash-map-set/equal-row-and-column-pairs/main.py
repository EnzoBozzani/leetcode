class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        m = {}

        n = len(grid)

        equal_pairs = 0

        for i in range(n):
            hash = ''
            for j in range(n):
                hash += f'{grid[j][i]}-'
            
            if hash in m:
                m[hash] += 1
            else:
                m[hash] = 1
        
        for i in range(n):
            hash = ''
            for j in range(n):
                hash += f'{grid[i][j]}-'
        
            if hash in m:
                equal_pairs += m[hash]
        
        return equal_pairs
        
        
        

if __name__ == '__main__':
    solution = Solution()
                        
    examples = [
        [[3,2,1],[1,7,6],[2,7,7]], 
        [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 
    ]

    for e in examples:
        print(e)
        print(solution.equalPairs(e))    
        print()                      

