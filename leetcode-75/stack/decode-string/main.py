class Solution:
    def decodeString(self, s: str) -> str:
        decoded = ''
        stack: list[tuple[str, int]] = []
        mult = 0

        for char in s:
            if char.isdigit():
                mult = (mult * 10) + int(char)
            elif char == '[':
                stack.append((decoded, mult))

                decoded = ''
                mult = 0
            elif char == ']':
                text, n = stack.pop()
                
                decoded = text + (decoded * n)
            else:
                decoded += char

        return decoded
            

if __name__ == '__main__':
    solution = Solution()
                        
    examples = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]

    for e in examples:
        print(e)
        print(solution.decodeString(e))    
        print()                      

