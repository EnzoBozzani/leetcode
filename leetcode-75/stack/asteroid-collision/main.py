class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for i in range(len(asteroids)):
            a = asteroids[i]

            if (len(stack) == 0): 
                stack.append(a)
                continue

            current = stack[-1]

            if a < 0 and current > 0:
                if abs(a) == abs(current):
                    stack.pop()
                elif abs(a) > abs(current):
                    stack.pop()

                    if (len(stack) == 0):
                        stack.append(a)
                        continue

                    current = stack[-1]

                    destroyed_both = False
                    stopped = False
                    
                    while (len(stack) > 0 and current > 0):
                        if abs(a) > abs(current):
                            stack.pop()

                            if (len(stack) == 0):
                                stack.append(a)
                                stopped = True
                                break

                            current = stack[-1]
                        elif abs(a) == abs(current):
                            stack.pop()
                            destroyed_both = True
                            break
                        else:
                            stopped = True
                            break
                    
                    if not destroyed_both and not stopped:                        
                        stack.append(a)

            else:
                stack.append(a)

        return stack

if __name__ == '__main__':
    solution = Solution()
                        
    examples = [[5,10,-5], [8,-8], [10,2,-5], [1,-2,-2,-2], [1,-1,-2,-2], [1,1,-2,-2]]

    for e in examples:
        print(e)
        print(solution.asteroidCollision(e))    
        print()                      

