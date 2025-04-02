# USAR PONTEIROS NO COMEÇO E FIM DE NUMS1 E NUMS2

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)            

        stop_index = ((len1 + len2) // 2) + 1

        i = 0
        j = 0

        nums = (None, None)

        while (i + j < stop_index):
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    nums = (nums1[i], nums[0])
                    i += 1
                else:
                    nums = (nums2[j], nums[0])
                    j += 1
            elif i < len1:
                nums = (nums1[i], nums[0])
                i += 1
            elif j < len2:
                nums = (nums2[j], nums[0])
                j += 1
            else: break

        if (len1 + len2) % 2 != 0:
            return nums[0]
            
        return (nums[0] + nums[1]) / 2

                

            


if __name__ == '__main__':
    solution = Solution()
                        
    examples = [[[1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17]], [[1,2], [3,4]]]

    for e in examples:
        print(e)
        print(solution.findMedianSortedArrays(e[0], e[1]))    
        print()                      

