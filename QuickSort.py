import sys

def Quick_Sort(list):
    if len(list) <= 1:
        return list

    leftList = []
    equalList = []
    RightList = []

    pivot = list[len(list)//2]

    for num in list:
        if num < pivot:
            leftList.append(num)
        elif num == pivot:
            equalList.append(num)
        else:
            RightList.append(num)

    return Quick_Sort(leftList) + equalList + Quick_Sort(RightList)

#1427번 문제 : 소트인사이드 문제

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    cnt = 0
    num = 1
    arr = []
    while n != 0:
        arr.append(n%10)
        n = n//10
        cnt+=1

    result = Quick_Sort(arr)

    ans = 0
    for i in range(0,cnt):
        ans += num * result[i]
        num = 10 * num

    print(ans)