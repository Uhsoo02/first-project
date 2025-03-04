num = int(input())
num_list = list(map(int, input().split()))
plus, minus, multi, division = map(int, input().split())
 
max_result = -1000000000
min_result = 1000000000
 
N = plus+minus+multi+division
check_list = [False]*N
count = 0
index = 0
result_list = []
 
def permutation(count, index, result):
    global max_result, min_result
    if count == N:
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
        return
 
    for i in range(N):
        if check_list[i] == True:
            continue
 
        check_list[i] = True
        if i <= plus - 1:
            permutation(count + 1, index + 1, result+num_list[index])
        elif i <= plus + minus - 1:
            permutation(count + 1, index + 1, result-num_list[index])
        elif i <= plus + minus + multi - 1:
            permutation(count + 1, index + 1, result*num_list[index])
        elif i <= plus + minus + multi + division - 1:
            if result < 0:
                permutation(count + 1, index + 1, -((-result)//num_list[index]))
            else:
                permutation(count + 1, index + 1, result//num_list[index])
        check_list[i] = False
 
permutation(0,1, num_list[0])
print(max_result)
print(min_result)
