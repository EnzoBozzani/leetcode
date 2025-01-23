import sys
import os

def main():
    args = sys.argv

    for i, arg in enumerate(args):
        if arg == '--path':
            if i + 1 >= len(args):
                print('Error: after --path, inform the value')
                sys.exit()

            os.makedirs(args[i + 1])

            with open(f'{args[i + 1]}/main.py', 'w') as f:
                f.write("""class Solution(object):
    def func(self):
        raise NotImplementedError()

if __name__ == '__main__':
    solution = Solution()
                        
    examples = []

    for e in examples:
        print(e)
        print(solution.func(e))    
        print()                      

""")
                
            print(f'{args[i + 1]}/main.py created successfully')

            sys.exit()

    print('Error: --path is required')
    sys.exit()

if __name__ == '__main__':
    main()