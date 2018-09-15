

if __name__ == '__main__':

    number = input().split()
    # print(number)
    left_sum = input().split()
    # print(left_sum)
    left_sum = [int(i) for i in left_sum]
    days = []
    for i in range(int(number[1])):
        days.append(input().split())
    # print(days)

    for item in days:
        if item[0] == 'A':
            left_sum[int(item[1])-1] += 1
        elif item[0] == 'B':
            left_sum[int(item[1])-1] -= 1
    want = left_sum[int(number[2]) - 1]
    left_sum.sort(reverse=True)
    print(left_sum.index(want)+1)
