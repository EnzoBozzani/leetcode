class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        map = {}

        for num in arr:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        unique_occurrences = {}
        
        for value in map.values():
            if value in unique_occurrences:
                return False
            else:
                unique_occurrences[value] = 1
        
        return True

if __name__ == '__main__':
    solution = Solution()
                        
    examples = [[1,2,2,1,1,3], [1,2], [-3,0,1,-3,1,1,1,-3,10,0]]

    for e in examples:
        print(e)
        print(solution.uniqueOccurrences(e))    
        print()                      

