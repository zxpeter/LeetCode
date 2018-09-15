
# aqiyi

number = int(input())
array = []
for i in range(number):
    a,b = list(map(int, input().split()))
    array.append([min(a,b), max(a,b)])
# print(array)

array_sorted = sorted(array, key=lambda x:x[1])

res = 1
j = array_sorted[0][1]
for item in array_sorted[1:]:
    if item[0] >= j:
        res += 1
        j = item[1]


# print(array_sorted)
print(res)


