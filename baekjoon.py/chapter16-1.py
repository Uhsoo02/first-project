import sys
N = int(sys.stdin.readline())
Stack = []
for i in range(N):
    Operation = sys.stdin.readline().split()
    if Operation[0] == '1':
        Stack.append(int(Operation[-1]))
    elif Operation[0] == '2':
        if Stack:
            print(Stack.pop(-1))
            continue
        print(-1)
    elif Operation[0] == '3':
        print(len(Stack))
    elif Operation[0] == '4':
        if Stack:
            print(0)
            continue
        print(1)
    elif Operation[0] == '5':
        if Stack:
            print(Stack[-1])
            continue
        print(-1)