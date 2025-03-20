class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        difference_map = {}

        for i, num in enumerate(nums):
            if num in difference_map:
                return [difference_map[num], i]
            else:
                difference_map[target - num] = i
        
        return []


if __name__ == '__main__':
    solution = Solution()
                        
    examples = [[[2,7,11,15], 9], [[3,2,4], 6], [[3,3], 6]]

    for e in examples:
        print(e)
        print(solution.twoSum(e[0], e[1]))    
        print()                      

