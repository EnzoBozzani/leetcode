class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0

        substr = ''
        current_length = 0

        for char in s:
            if char not in substr:
                substr += char
                current_length += 1

                if current_length > longest_length: 
                    longest_length = current_length
            else:
                index = substr.find(char)
                
                substr = substr[index + 1:] + char

                current_length = len(substr)

                if current_length > longest_length: 
                    longest_length = current_length

        return longest_length

if __name__ == '__main__':
    solution = Solution()
                        
    examples = ["abcabcbb", "bbbbb", "pwwkew", "aabaab!bb"]

    for e in examples:
        print(e, end=" ")
        print(solution.lengthOfLongestSubstring(e))    
        print()                      

