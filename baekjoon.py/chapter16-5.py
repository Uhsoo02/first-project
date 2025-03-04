N = int(input())

student = list(map(int,input().split()))

stack = []

now_turn = 1
for students in student:
    stack.append(students)
    while stack and stack[-1] == now_turn:
        stack.pop()
        now_turn += 1

if stack:
    print('Sad')
else:
    print('Nice')