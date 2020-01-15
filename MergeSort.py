import sys

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

#1427번 문제 : 소트인사이드 문

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cnt = 0
    num = 1
    arr = []
    while n != 0:
        arr.append(n%10)
        n = n//10
        cnt+=1

    result = merge_sort(arr)

    ans = 0
    for i in range(0,cnt):
        ans += num * result[i]
        num = 10 * num

    print(ans)