class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = []
        length = 0

        for char in senate:
            queue.append(char)
            length += 1

        senators = {
            'R': 0,
            'D': 0
        }

        bans = {
            'R': 0,
            'D': 0
        }

        first_round = True
        i = 0

        while (True):
            senator = queue[i]

            if first_round:
                senators[senator] += 1

            if bans[senator] > 0:
                bans[senator] -= 1
                queue.pop(i)
                senators[senator] -= 1
                length -= 1
                i -= 1
            else:
                oponent = 'D' if senator == 'R' else 'R'
                bans[oponent] += 1

            if (i + 1 >= length):
                first_round = False

                if senators['D'] == 0:
                    return 'Radiant'
                if senators['R'] == 0:
                    return 'Dire'

                i = 0
            else:
                i += 1



if __name__ == '__main__':
    solution = Solution()
                        
    examples = ["DDDRRRRR", "RD", "DRRDRDRDRDDRDRDR"]

    for e in examples:
        print(e)
        print(solution.predictPartyVictory(e))    
        print()                      

