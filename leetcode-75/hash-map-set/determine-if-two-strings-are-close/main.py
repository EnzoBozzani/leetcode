class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map1 = {}
        map2 = {}

        for char in word1:
            if char not in word2:
                return False
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1
    
        for char in word2:
            if char not in map1:
                return False
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 1

        word1_occurrences = {}
        word2_occurrences = {}

        for value in map1.values():
            if value in word1_occurrences:
                word1_occurrences[value] += 1
            else:
                word1_occurrences[value] = 1
        
        for value in map2.values():
            if value in word2_occurrences:
                word2_occurrences[value] += 1
            else:
                word2_occurrences[value] = 1

        for key, value in word1_occurrences.items():
            if key not in word2_occurrences:
                return False
            if value != word2_occurrences[key]:
                return False
            
        return True
                

if __name__ == '__main__':
    solution = Solution()
                        
    examples = [["abc", "bca"], ["a", "aa"], ["cabbba", "abbccc"], ["uau", "ssx"], ["abc", "abcdd"]]

    for e in examples:
        print(e)
        print(solution.closeStrings(e[0], e[1]))    
        print()                      

