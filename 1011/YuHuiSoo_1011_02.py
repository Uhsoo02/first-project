# 과제2: 버블 정렬 with Python (튜플로 수정할 것),  강의노트[4] p.36
# 이름: 유희수
# 날짜: 2024.10.11

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
            print(array)

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
bubble_sort(array)