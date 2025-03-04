# 과제6: 이진 탐색과 보간 탐색의 성능비교
# 이름: 컴퓨터공학부 유희수
# 날짜: 2024-11-08

import random

def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high and key >= arr[low] and key <= arr[high]:
        count += 1

        if low == high:
            if arr[low] == key:
                print(f"보간 탐색 비교 횟수: {count}")
                return low
            print(f"보간 탐색 비교 횟수: {count}")
            return -1
        
        mid = low + ((high - low) * (key-arr[low])) // (arr[high] - arr[low])

        if arr[mid] == key:
            print(f"보간 탐색 비교 횟수: {count}")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print(f"보간 탐색 비교 횟수: {count}")
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            print(f"이진 탐색 비교 횟수: {count}")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
        
    print(f"이진 탐색 비교 횟수: {count}")
    return -1

arr = sorted(random.sample(range(1, 101), 20))

print("정렬된 배열: ", arr)