

def find_combine(m,n,item,items_set):
    if m <= 0 or n <= 0:
        return
    if m == n:
        items_set.append(item + [n])
    item.append(n)
    find_combine(m-n, n-1, item,items_set)
    item.pop()
    find_combine(m, n-1, item, items_set)


if __name__ == '__main__':
    m = 10
    n = 9
    item = []
    items_set = []
    find_combine(m,n,item, items_set)
    print(items_set)

