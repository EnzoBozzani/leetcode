class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        n1 = list(set(nums1))
        n2 = list(set(nums2))

        answer = [[], []]

        for i in range(len(n1)):
            if n1[i] not in n2:
               answer[0].append(n1[i])

        for i in range(len(n2)):
            if n2[i] not in n1:
               answer[1].append(n2[i])
            
        return answer


if __name__ == '__main__':
    solution = Solution()
                        
    examples: list[tuple[list[int], list[int]]] = [[[1,2,3], [2,4,6]], [[1,2,3,3], [1,1,2,2]]]

    for e in examples:
        print(e)
        print(solution.findDifference(e[0], e[1]))    
        print()          

