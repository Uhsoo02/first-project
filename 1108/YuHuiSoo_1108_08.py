# 과제8:  퀵 정렬(파이썬 장점을 살린 방식) - Step과 Pivot 표시
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-08

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
step = 1

def quick_sort(array):
    global step

    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    display_array = ["*" + str(pivot)] + tail
    print(f"Swtp {step}:", display_array)
    step += 1

    left_side = [x for x in tail if x < pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

sorted_array = quick_sort(array)
print("Final sorted array:", sorted_array)